# Django ORM — Complete Learning Notes (Cinema Project)

These notes follow a **progressive learning path**: from basic querying to advanced relationships, aggregation, and optimization. We use your actual cinema models throughout.

---

## Your Models

```python
from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name + self.location


class CinemaHall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cinema}-{self.name}"


class Seat(models.Model):
    name = models.CharField(max_length=10)
    cinemahall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    cinemahall = models.ForeignKey(CinemaHall, on_delete=models.PROTECT)
    show_time = models.DateTimeField()
    price = models.PositiveIntegerField()

    class Meta:
        unique_together = ("cinemahall", "movie", "show_time")

    def __str__(self):
        return f"{self.movie} - {self.cinemahall}"


class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    show = models.ForeignKey(Show, on_delete=models.PROTECT)
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT)

    class Meta:
        unique_together = ("show", "seat")

    def __str__(self):
        return self.customer.first_name
```

**Relationship map:**

```text
Cinema
  └── CinemaHall (FK: cinema)
        ├── Seat (FK: cinemahall)
        └── Show (FK: cinemahall)
              └── Movie (FK: movie)
                    └── Reservation (FK: show, seat, customer → User)
```

---

# Stage 1 — Normal Querying (No Relationships Yet)

Forget `related_name`, forget optimization. Just learn to fetch and filter.

### Get everything

```python
Movie.objects.all()
```

### Get one specific object

```python
Movie.objects.get(id=1)
Movie.objects.get(pk=1)   # pk = primary key, same as id here
```

### `get()` vs `filter()`

| | Returns | Use when |
|---|---|---|
| `get()` | A single object | You expect exactly one match |
| `filter()` | A QuerySet (list-like) | You expect zero, one, or many matches |

```python
Movie.objects.get(id=1)        # <Movie: Avatar>
Movie.objects.filter(id=1)     # <QuerySet [<Movie: Avatar>]>
```

`get()` raises errors if it doesn't get exactly one match:
- `DoesNotExist` → no match found
- `MultipleObjectsReturned` → more than one match found

### Filtering

```python
Movie.objects.filter(genre="Action")
```

Multiple conditions = **AND**:

```python
Movie.objects.filter(genre="Action", name="Batman")
# genre = "Action" AND name = "Batman"
```

### Excluding

```python
Movie.objects.exclude(genre="Horror")
# everything EXCEPT horror movies
```

### Ordering

```python
Movie.objects.order_by("name")     # A → Z
Movie.objects.order_by("-name")    # Z → A
Movie.objects.order_by("genre", "name")  # genre first, then name
```

### Limiting results

```python
Movie.objects.all()[:5]                  # first 5
Movie.objects.order_by("name")[:5]       # first 5, alphabetically
```

### `first()` and `last()`

```python
Movie.objects.order_by("name").first()   # returns None if empty (no error)
Movie.objects.order_by("name").last()
```

### Checking existence (efficient — no full fetch)

```python
Show.objects.filter(price__gt=500).exists()   # True / False
```

### ✅ Practice checklist for Stage 1

```python
Movie.objects.all()
Movie.objects.get(id=1)
Movie.objects.filter(genre="Action")
Movie.objects.exclude(genre="Horror")
Movie.objects.order_by("name")
Movie.objects.order_by("-name")
Movie.objects.filter(...).first()
Movie.objects.filter(...).exists()
```

---

# Stage 2 — Field Lookups

Pattern: `field__lookup=value`

### Text lookups

```python
Movie.objects.filter(name__exact="Batman")       # exact match
Movie.objects.filter(name__iexact="batman")       # case-insensitive exact
Movie.objects.filter(name__contains="bat")        # case-sensitive substring
Movie.objects.filter(name__icontains="bat")       # case-insensitive substring
Movie.objects.filter(name__startswith="Bat")
Movie.objects.filter(name__endswith="man")
```

### Number/date comparison lookups

```python
Show.objects.filter(price__gt=500)     # >
Show.objects.filter(price__gte=500)    # >=
Show.objects.filter(price__lt=500)     # <
Show.objects.filter(price__lte=500)    # <=
```

### Range

```python
Show.objects.filter(price__range=(300, 500))
# 300 <= price <= 500
```

### `in`

```python
Movie.objects.filter(genre__in=["Action", "Comedy"])
```

### ✅ Practice checklist for Stage 2

```python
Movie.objects.filter(name__icontains="bat")
Movie.objects.filter(genre__in=["Action", "Comedy"])
Show.objects.filter(price__gt=500)
Show.objects.filter(price__range=(300, 500))
Show.objects.order_by("-price")
```

---

# Stage 3 — Forward ForeignKey Access

You already have an object → just access the related field like a normal Python attribute.

```python
show = Show.objects.get(id=1)

show.movie          # <Movie: Avatar>
show.movie.name      # "Avatar"
show.cinemahall       # <CinemaHall: ...>
show.cinemahall.cinema.name   # follow it two levels deep
```

This works because `movie` and `cinemahall` are **ForeignKey fields on Show**. No special syntax needed — just `.`.

Similarly:

```python
seat = Seat.objects.get(id=1)
seat.cinemahall.cinema.location   # Seat → CinemaHall → Cinema → location
```

---

# Stage 4 — Traversing Relationships Inside `filter()`

Now the double underscore (`__`) means something new: **"follow this relationship."**

> Give me all shows whose movie's genre is "Action".

```python
Show.objects.filter(movie__genre="Action")
```

Read it as a path:

```text
Show → movie → genre == "Action"
```

More examples using your models:

```python
# Shows happening in a specific cinema (by cinema name)
Show.objects.filter(cinemahall__cinema__name="PVR")

# Seats belonging to a specific cinema
Seat.objects.filter(cinemahall__cinema__name="INOX")

# Reservations for Action movies — 3 levels deep
Reservation.objects.filter(show__movie__genre="Action")

# Reservations made by a user with a specific username
Reservation.objects.filter(customer__username="john123")
```

You can mix a relationship traversal with a lookup:

```python
Show.objects.filter(movie__name__icontains="bat")
# Show → movie → name (icontains "bat")
```

---

# Stage 5 — Reverse Relationships

Forward access (`show.movie`) is easy because the ForeignKey is *defined* on `Show`. But what if you're standing on `Movie` and want its `Show`s? That relationship isn't explicitly written anywhere on `Movie` — Django creates it automatically, in reverse.

```python
movie = Movie.objects.get(id=1)

movie.show_set.all()     # all Shows for this movie
```

Since you didn't set `related_name` on the `movie` field in `Show`, Django defaults to:

```text
<lowercase model name>_set
```

So:

```python
cinema = Cinema.objects.get(id=1)
cinema.cinemahall_set.all()     # all CinemaHalls in this cinema

cinemahall = CinemaHall.objects.get(id=1)
cinemahall.seat_set.all()       # all Seats in this hall
cinemahall.show_set.all()       # all Shows in this hall

show = Show.objects.get(id=1)
show.reservation_set.all()      # all Reservations for this show

user = User.objects.get(id=1)
user.reservation_set.all()      # all Reservations made by this user
```

---

# Stage 6 — `related_name`

`movie.show_set` works, but the name is ugly. This is the actual problem `related_name` solves — you're not learning it as a rule to memorize, you're fixing something you've already run into.

```python
class Show(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name="shows"
    )
    cinemahall = models.ForeignKey(
        CinemaHall,
        on_delete=models.PROTECT,
        related_name="shows"
    )
```

Now instead of `movie.show_set.all()`, you get:

```python
movie.shows.all()
cinemahall.shows.all()
```

**Suggested `related_name`s for your project:**

```python
# Cinema
cinema = models.ForeignKey(Cinema, on_delete=models.PROTECT, related_name="halls")

# Seat
cinemahall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, related_name="seats")

# Show
movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name="shows")
cinemahall = models.ForeignKey(CinemaHall, on_delete=models.PROTECT, related_name="shows")

# Reservation
customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="reservations")
show = models.ForeignKey(Show, on_delete=models.PROTECT, related_name="reservations")
seat = models.ForeignKey(Seat, on_delete=models.PROTECT, related_name="reservations")
```

Resulting usage:

```python
cinema.halls.all()
cinemahall.seats.all()
movie.shows.all()
cinemahall.shows.all()
user.reservations.all()
show.reservations.all()
seat.reservations.all()
```

> ⚠️ Note: `related_name` also affects reverse lookups inside `filter()`. If you set `related_name="shows"` on `Show.movie`, then you must use `movie__shows__...` (not `movie__show_set__...`) when filtering *from* `Movie` toward `Show` in reverse. Forward traversal (`Show.objects.filter(movie__genre=...)`) is unaffected.

---

# Stage 7 — Reverse Traversal Inside `filter()`

Once you have `related_name`, you can also query "backwards" starting from the "one" side.

```python
# Movies that have at least one show priced above 1000
Movie.objects.filter(shows__price__gt=1000)

# Cinemas that have a hall named "Hall 1"
Cinema.objects.filter(halls__name="Hall 1")

# Users who have reserved a seat for an Action movie
User.objects.filter(reservations__show__movie__genre="Action")
```

⚠️ Reverse traversal across a "many" relationship can produce **duplicate rows** if a Movie has multiple matching Shows. Use `.distinct()` when needed:

```python
Movie.objects.filter(shows__price__gt=1000).distinct()
```

---

# Stage 8 — `select_related()` and `prefetch_related()` (Performance)

### The problem: N+1 queries

```python
shows = Show.objects.all()
for show in shows:
    print(show.movie.name)   # 1 query per show!
```

If there are 100 shows, this fires **101 queries** (1 for the list, 100 for each `.movie` access).

### `select_related()` — for ForeignKey / OneToOne (forward, "one" side)

Performs a SQL `JOIN` in a single query.

```python
shows = Show.objects.select_related("movie", "cinemahall")
for show in shows:
    print(show.movie.name)   # no extra query
```

You can chain across relationships:

```python
Show.objects.select_related("cinemahall__cinema")
```

### `prefetch_related()` — for reverse FK / ManyToMany ("many" side)

Runs a **separate optimized query** and joins the results in Python.

```python
movies = Movie.objects.prefetch_related("shows")
for movie in movies:
    print(movie.shows.all())   # no extra query per movie
```

### Combine both

```python
Reservation.objects.select_related(
    "customer", "show__movie", "seat__cinemahall"
)
```

**Rule of thumb:**

| Relationship type | Use |
|---|---|
| ForeignKey / OneToOne (forward) | `select_related()` |
| Reverse FK / ManyToMany | `prefetch_related()` |

---

# Stage 9 — `Q()` Objects (OR conditions)

`filter(a=1, b=2)` only gives you AND. For OR, NOT, or complex combinations, use `Q`.

```python
from django.db.models import Q

# Movies that are Action OR Comedy
Movie.objects.filter(Q(genre="Action") | Q(genre="Comedy"))

# Shows that are NOT priced above 1000
Show.objects.filter(~Q(price__gt=1000))

# Action movies OR movies with "man" in the name, but priced under 500
Show.objects.filter(
    (Q(movie__genre="Action") | Q(movie__name__icontains="man"))
    & Q(price__lt=500)
)
```

---

# Stage 10 — `annotate()` and `aggregate()`

### `aggregate()` — one summary value for the whole QuerySet

```python
from django.db.models import Count, Sum, Avg, Max, Min

Show.objects.aggregate(Avg("price"))
# {'price__avg': 450.0}

Reservation.objects.aggregate(total=Count("id"))
# {'total': 230}
```

### `annotate()` — a value added to *each* object in the QuerySet

```python
# Number of shows per movie
Movie.objects.annotate(show_count=Count("shows"))

for movie in Movie.objects.annotate(show_count=Count("shows")):
    print(movie.name, movie.show_count)

# Total revenue per show (price * number of reservations)
Show.objects.annotate(seats_booked=Count("reservations"))

# Movies with more than 5 shows
Movie.objects.annotate(show_count=Count("shows")).filter(show_count__gt=5)
```

---

# Stage 11 — `F()` Expressions and Conditional Logic

### `F()` — reference another field's value in the database itself

```python
from django.db.models import F

# Increase every show's price by 50, in one SQL query
Show.objects.update(price=F("price") + 50)

# Compare two fields on the same row
Show.objects.filter(price__gt=F("cinemahall__seats__count"))
```

### `Case` / `When` — conditional values

```python
from django.db.models import Case, When, Value, CharField

Show.objects.annotate(
    price_tier=Case(
        When(price__gte=1000, then=Value("Premium")),
        When(price__gte=500, then=Value("Standard")),
        default=Value("Budget"),
        output_field=CharField(),
    )
)
```

---

# Stage 12 — `Subquery`, `OuterRef`, `Exists`

For advanced correlated subqueries.

```python
from django.db.models import Subquery, OuterRef, Exists

# Latest show time per movie
latest_show = Show.objects.filter(
    movie=OuterRef("pk")
).order_by("-show_time")

Movie.objects.annotate(
    latest_show_time=Subquery(latest_show.values("show_time")[:1])
)

# Movies that have at least one show (efficient existence check)
has_show = Show.objects.filter(movie=OuterRef("pk"))
Movie.objects.annotate(has_show=Exists(has_show)).filter(has_show=True)
```

---

# Stage 13 — Production Concerns

### Transactions

```python
from django.db import transaction

with transaction.atomic():
    reservation = Reservation.objects.create(customer=user, show=show, seat=seat)
    # if anything below fails, the reservation is rolled back too
```

### Preventing double-booking with `select_for_update`

```python
with transaction.atomic():
    seat = Seat.objects.select_for_update().get(id=seat_id)
    # locks this row until the transaction commits — prevents race conditions
    Reservation.objects.create(customer=user, show=show, seat=seat)
```

### `unique_together` (already in your models)

```python
class Show(models.Model):
    class Meta:
        unique_together = ("cinemahall", "movie", "show_time")

class Reservation(models.Model):
    class Meta:
        unique_together = ("show", "seat")
```

This makes the database itself reject duplicate bookings — one seat can't be reserved twice for the same show.

### Indexes

```python
class Show(models.Model):
    show_time = models.DateTimeField(db_index=True)
```

Speeds up filtering/ordering on frequently-queried fields.

### Inspecting the actual SQL

```python
print(Show.objects.filter(price__gt=500).query)
```

---

# Full Progression Summary

| Stage | Concept | Example |
|---|---|---|
| 1 | Basic querying | `Movie.objects.filter(genre="Action")` |
| 2 | Field lookups | `name__icontains`, `price__gt` |
| 3 | Forward FK access | `show.movie.name` |
| 4 | Relationship traversal in filter | `Show.objects.filter(movie__genre="Action")` |
| 5 | Reverse relationships (default) | `movie.show_set.all()` |
| 6 | `related_name` | `movie.shows.all()` |
| 7 | Reverse traversal in filter | `Movie.objects.filter(shows__price__gt=1000)` |
| 8 | Query optimization | `select_related()`, `prefetch_related()` |
| 9 | OR logic | `Q()` |
| 10 | Aggregation | `annotate()`, `aggregate()`, `Count()` |
| 11 | DB-level expressions | `F()`, `Case()`, `When()` |
| 12 | Correlated subqueries | `Subquery()`, `OuterRef()`, `Exists()` |
| 13 | Production readiness | transactions, locking, constraints, indexes |

---

### Suggested Practice Exercises

1. Get all shows for a movie named "Avatar", ordered by price descending.
2. Find all cinema halls in a cinema called "PVR" that have more than 50 seats.
3. Find all users who have made more than 3 reservations.
4. Find the total revenue (sum of show prices across all reservations) per cinema.
5. Rewrite exercise 1–4 with `select_related`/`prefetch_related` and check the query count using `django.db.connection.queries` or Django Debug Toolbar.
