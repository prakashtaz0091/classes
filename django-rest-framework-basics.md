# Django REST Framework — Practical Notes

---

## 1. `@api_view` vs `APIView`

Both let you write **function-based** or **class-based** views, but wrapped differently.

### `@api_view` (function-based)
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
```

### `APIView` (class-based)
```python
from rest_framework.views import APIView
from rest_framework.response import Response

class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
```

**Key difference:** `@api_view` just turns a plain function into a DRF-aware view (adds request parsing, content negotiation, etc.). `APIView` is a class — HTTP methods become class methods (`get`, `post`, `put`, `delete`), giving you more structure (mixins, inheritance, `self`).

📖 [api_view docs](https://www.django-rest-framework.org/api-guide/views/#function-based-views) | [APIView docs](https://www.django-rest-framework.org/api-guide/views/#class-based-views)

---

## 2. Function-Based vs Class-Based Views — When to Choose

| Use FBV (`@api_view`) when... | Use CBV (`APIView`/Generics/ViewSets) when... |
|---|---|
| Logic is simple, one-off, non-CRUD (e.g. a custom "send OTP" endpoint) | You're doing standard CRUD |
| You want explicit, top-to-bottom control | You want to reuse behavior via inheritance/mixins |
| Very small project / quick script | Medium-to-large project, many similar models |
| Easier for beginners to read line-by-line | You want less repeated code (DRY) |

**Rule of thumb:** if it's CRUD on a model → go class-based (Generics/ViewSets). If it's a weird one-off action → FBV or `@action` inside a ViewSet.

---

## 3. Generic Views vs ViewSets vs ModelViewSet

### a) Individual Generic Views
Use when each endpoint needs **different behavior/permissions/serializers**, or you don't want all CRUD operations exposed.

```python
from rest_framework import generics

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```
urls.py needs manual registration:
```python
path('students/', StudentListCreate.as_view()),
path('students/<int:pk>/', StudentDetail.as_view()),
```

**When to use:** you need fine control per-endpoint (e.g., different permissions for list vs create), or only want a subset of CRUD (e.g., only GET + POST, no DELETE).

### b) ViewSet / ModelViewSet
Use when you want **full standard CRUD** for a model with minimal code, and you're happy to let a `Router` auto-generate the URLs.

```python
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```
That's it — `ModelViewSet` gives you list, create, retrieve, update, partial_update, destroy — all in one class.

**When to use:**
- `ModelViewSet` → standard full CRUD, fastest to write.
- `ViewSet` (plain) → you want CRUD-*like* structure but with fully custom logic per method (no default queryset behavior).
- `ReadOnlyModelViewSet` → only list + retrieve (no write ops), e.g. public read-only data.

📖 [Generic views](https://www.django-rest-framework.org/api-guide/generic-views/) | [ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)

---

## 4. What Goes Inside Serializers?

Serializers handle: **validation, conversion (Python ⇄ JSON), and object creation/update.**

```python
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'age']

    # field-level validation
    def validate_age(self, value):
        if value < 5:
            raise serializers.ValidationError("Age too low")
        return value

    # object-level validation (multiple fields together)
    def validate(self, data):
        if data['name'] == '' :
            raise serializers.ValidationError("Name required")
        return data

    # custom create/update logic (e.g. hashing password, nested writes)
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
```

**Put inside serializers:**
- Field definitions / `Meta` class
- Validation (`validate_<field>`, `validate`)
- `create()` / `update()` overrides for custom save logic
- Nested serializers for related objects

**Do NOT put inside serializers:** permission checks, request/response handling, business logic unrelated to data shape — that belongs in the view.

---

## 5. What Goes Inside Views?

Views handle: **request → response flow, permission/auth checks, calling serializers, querysets.**

```python
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # filter by logged-in user, query params, etc.
        return Student.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # inject extra data at save time (not from client)
        serializer.save(owner=self.request.user)
```

**Put inside views:**
- `queryset` / `get_queryset()` — what data to fetch
- `permission_classes`, `authentication_classes`
- `perform_create` / `perform_update` / `perform_destroy` — hook points to inject extra data (e.g. `request.user`)
- Overriding `get`, `post`, etc. only when you need custom response logic

---

## 6. Custom Actions in ViewSets — `@action`

For endpoints that aren't plain CRUD (e.g. `/students/5/activate/`).

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        student = self.get_object()
        student.is_active = True
        student.save()
        return Response({'status': 'activated'})

    @action(detail=False, methods=['get'])
    def top_scorers(self, request):
        students = self.get_queryset().order_by('-score')[:5]
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)
```

- `detail=True` → acts on a single object → URL: `/students/{pk}/activate/`
- `detail=False` → acts on the collection → URL: `/students/top_scorers/`

📖 [Routing extra actions](https://www.django-rest-framework.org/api-guide/routers/#routing-for-extra-actions-with-action-decorator)

---

## 7. Routers

Routers auto-generate URLs for ViewSets (list/detail/custom actions) — saves you from writing `urlpatterns` by hand.

```python
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')

urlpatterns = router.urls
```

This auto-creates:
```
GET/POST      /students/
GET/PUT/PATCH/DELETE  /students/{pk}/
+ any @action endpoints
```

- `DefaultRouter` → adds a browsable API root view listing all routes.
- `SimpleRouter` → same thing, no root view.

**Only use routers with ViewSets** — not with plain `APIView`/Generic views (those need manual `path()`).

📖 [Routers docs](https://www.django-rest-framework.org/api-guide/routers/)

---

## 8. Types of Serializers

| Serializer | Use case |
|---|---|
| `Serializer` | Full manual control — define every field yourself, no model tie-in required |
| `ModelSerializer` | Auto-generates fields from a model — most common, saves time |
| `HyperlinkedModelSerializer` | Like `ModelSerializer` but uses hyperlinks instead of PK for relations |
| `ListSerializer` | Internally used when `many=True` — handles serializing lists of objects |

```python
# Plain Serializer — full control
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
```

Use `ModelSerializer` 95% of the time. Use plain `Serializer` when data doesn't map to a model (e.g. validating a contact-form payload, custom aggregated data).

📖 [Serializers docs](https://www.django-rest-framework.org/api-guide/serializers/)

---

## 9. Serializer Fields & Read-Only Fields

```python
class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()      # computed, read-only
    id = serializers.IntegerField(read_only=True)         # explicit read-only
    password = serializers.CharField(write_only=True)     # never sent back in response

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'password', 'full_name']
        read_only_fields = ['email']   # shortcut instead of declaring field manually

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
```

- `read_only=True` → field is included in output, ignored on input (e.g. `id`, auto timestamps).
- `write_only=True` → accepted on input, excluded from output (e.g. `password`).
- `SerializerMethodField()` → always read-only, computed via `get_<field_name>()`.
- `Meta.read_only_fields = [...]` → quick way to mark multiple `ModelSerializer` fields read-only without redeclaring them.

Common field types: `CharField`, `IntegerField`, `BooleanField`, `DateTimeField`, `EmailField`, `ChoiceField`, `PrimaryKeyRelatedField` (for FK relations), `SlugRelatedField`, `SerializerMethodField`.

📖 [Serializer fields docs](https://www.django-rest-framework.org/api-guide/fields/)

---

## 10. Permission Classes

```python
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
```

| Class | Meaning |
|---|---|
| `AllowAny` | No restriction (default open) |
| `IsAuthenticated` | Must be logged in |
| `IsAdminUser` | Must be staff |
| `IsAuthenticatedOrReadOnly` | Anyone can GET, only logged-in can write |
| Custom `BasePermission` subclass | Your own rule (e.g. object owner only) |

Custom example:
```python
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
```

Set globally in `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated']
}
```

📖 [Permissions docs](https://www.django-rest-framework.org/api-guide/permissions/)

---

## 11. Authentication Classes

**Authentication ≠ Permission.** Authentication identifies *who* is making the request; permission decides *what they're allowed to do*.

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

| Class | Use case |
|---|---|
| `SessionAuthentication` | Browsable API / same-site browser clients (uses Django session + CSRF) |
| `TokenAuthentication` | Simple token-based auth for mobile/external clients (`Authorization: Token <key>`) |
| `JWTAuthentication` (via `djangorestframework-simplejwt`) | Stateless, industry-standard for SPAs/mobile — most commonly used in real projects |
| `BasicAuthentication` | Username/password on every request — mainly for testing, not production |

Token auth setup:
```python
INSTALLED_APPS = [..., 'rest_framework.authtoken']
# then: python manage.py migrate
# generate token: Token.objects.create(user=some_user)
```

You can also set per-view:
```python
class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
```

📖 [Authentication docs](https://www.django-rest-framework.org/api-guide/authentication/)

---

## 12. Pagination

Without pagination, a `list` endpoint returns *everything* — bad for large tables.

```python
# settings.py — applies globally
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```
Response becomes:
```json
{
  "count": 53,
  "next": "http://api.example.com/students/?page=2",
  "previous": null,
  "results": [ ... ]
}
```

| Class | Behavior |
|---|---|
| `PageNumberPagination` | `?page=2` — simplest, most common |
| `LimitOffsetPagination` | `?limit=10&offset=20` — more flexible slicing |
| `CursorPagination` | Opaque cursor — best for large/real-time-changing datasets (no page-skipping issues) |

Custom per-view:
```python
class StudentPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'   # client can override, e.g. ?page_size=20
    max_page_size = 50

class StudentViewSet(viewsets.ModelViewSet):
    pagination_class = StudentPagination
```

📖 [Pagination docs](https://www.django-rest-framework.org/api-guide/pagination/)

---

## 13. Filtering, Searching, Ordering

```bash
pip install django-filter
```
```python
INSTALLED_APPS = [..., 'django_filters']

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}
```

```python
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['age', 'is_active']    # exact-match filters -> ?age=20
    search_fields = ['name', 'email']          # partial text search -> ?search=john
    ordering_fields = ['name', 'age']          # -> ?ordering=-age
```

- `filterset_fields` → exact filtering on fields.
- `search_fields` → case-insensitive partial match (`?search=` query param).
- `ordering_fields` → sortable fields (`?ordering=field` or `?ordering=-field` for descending).

📖 [Filtering docs](https://www.django-rest-framework.org/api-guide/filtering/)

---

## 14. Throttling

Rate-limits how many requests a user/IP can make — protects against abuse.

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '20/minute',
        'user': '100/minute',
    }
}
```

- `AnonRateThrottle` → limits unauthenticated requests (by IP).
- `UserRateThrottle` → limits authenticated requests (by user).
- `ScopedRateThrottle` → different rate per specific view (via `throttle_scope = 'uploads'`).

Per-view override:
```python
class StudentViewSet(viewsets.ModelViewSet):
    throttle_classes = [UserRateThrottle]
```

📖 [Throttling docs](https://www.django-rest-framework.org/api-guide/throttling/)

---

## 15. Nested Serializers

Used when a model has related objects you want to serialize together (e.g. an `Author` with their `Book`s).

```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'published_year']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)   # reverse FK relation

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
```

Read-only nested output is easy (as above). **Writable nested serializers** need manual `create()`/`update()` since DRF doesn't handle nested writes automatically:

```python
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        books_data = validated_data.pop('books')
        author = Author.objects.create(**validated_data)
        for book_data in books_data:
            Book.objects.create(author=author, **book_data)
        return author
```

📖 [Nested relationships docs](https://www.django-rest-framework.org/api-guide/relations/#nested-relationships)

---

## 16. `Response` vs `HttpResponse`, and `request.data`

Always use DRF's own classes inside DRF views — they handle content negotiation (JSON, browsable API, etc.) automatically.

```python
from rest_framework.response import Response
from rest_framework import status

return Response({'message': 'created'}, status=status.HTTP_201_CREATED)
```

- `Response` (DRF) — renders based on client's `Accept` header (JSON by default, HTML in browsable API). Use this, **not** Django's `HttpResponse`/`JsonResponse`.
- `request.data` (DRF) — parses JSON, form-data, multipart — anything. Use this, **not** Django's `request.POST` (which only handles form-encoded data).
- `status` module — use named constants (`status.HTTP_404_NOT_FOUND`) instead of raw numbers like `404` — more readable and less error-prone.

---

## 17. Exception Handling

DRF automatically converts common exceptions into proper HTTP error responses — you rarely need manual `try/except`.

```python
from rest_framework.exceptions import NotFound, ValidationError

def get_object(self):
    try:
        return Student.objects.get(pk=self.kwargs['pk'])
    except Student.DoesNotExist:
        raise NotFound("Student not found")
```

Built-in exceptions DRF handles for you: `ValidationError` (400), `NotFound` (404), `PermissionDenied` (403), `NotAuthenticated` (401), `MethodNotAllowed` (405), `Throttled` (429).

You can customize the global handler in `settings.py`:
```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'myapp.utils.custom_exception_handler'
}
```

📖 [Exception handling docs](https://www.django-rest-framework.org/api-guide/exceptions/)

---

## 18. Browsable API

Every DRF endpoint automatically gets a built-in HTML UI (visit the URL directly in a browser) — lets you test GET/POST/PUT/DELETE with forms, no Postman needed during development. Enabled by default via `BrowsableAPIRenderer`. Great for quick manual testing and demoing to teammates.

---

## 19. Versioning

Plan for API evolution before breaking changes hit production clients.

```python
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning'
}
```
```python
# urls.py
path('api/<str:version>/students/', StudentList.as_view()),
```
```python
# inside a view
def get(self, request, *args, **kwargs):
    if request.version == 'v1':
        ...
```

| Strategy | Example |
|---|---|
| `URLPathVersioning` | `/api/v1/students/` |
| `NamespaceVersioning` | Django URL namespaces per version |
| `AcceptHeaderVersioning` | `Accept: application/json; version=1.0` |
| `QueryParameterVersioning` | `/api/students/?version=1.0` |

📖 [Versioning docs](https://www.django-rest-framework.org/api-guide/versioning/)

---

### Quick Decision Cheat Sheet

```
Simple one-off endpoint?              → @api_view
Standard CRUD, need per-endpoint control? → Generic Views (ListCreateAPIView, etc.)
Standard CRUD, want it fast & auto-routed? → ModelViewSet + Router
Only reading, no writes?              → ReadOnlyModelViewSet
Need a non-CRUD action on a resource? → @action inside ViewSet
```
