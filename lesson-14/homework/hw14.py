# parse_students.py
import json
import sys
from pathlib import Path

def print_student(student):
    # adapt to expected keys
    name = student.get("name", "<no name>")
    sid = student.get("id", "<no id>")
    age = student.get("age", "<no age>")
    courses = student.get("courses", [])
    print(f"Student: {name} (ID: {sid})")
    print(f"  Age: {age}")
    if courses:
        print("  Courses:")
        for c in courses:
            print(f"   - {c}")
    else:
        print("  Courses: none listed")
    print("-" * 40)

def main(path="students.json"):
    p = Path(path)
    if not p.exists():
        print(f"Error: file not found: {p}", file=sys.stderr)
        return

    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print("Error reading/parsing JSON:", e, file=sys.stderr)
        return

    # Accept either a dict with "students" key or a list
    if isinstance(data, dict):
        students = data.get("students") or data.get("Students") or []
    elif isinstance(data, list):
        students = data
    else:
        print("Unexpected JSON structure", file=sys.stderr)
        return

    if not students:
        print("No students found.")
        return

    for s in students:
        print_student(s)

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Print students from students.json")
    ap.add_argument("file", nargs="?", default="students.json", help="Path to students.json")
    args = ap.parse_args()
    main(args.file)

# weather_tashkent.py
import requests
import os
import sys

API_KEY = os.environ.get("OPENWEATHER_API_KEY")  # recommended
# or set here directly:
# API_KEY = "your_openweather_api_key_here"

if not API_KEY:
    print("Please set OPENWEATHER_API_KEY environment variable (or edit the script).", file=sys.stderr)
    sys.exit(1)

def get_current_weather(city="Tashkent", units="metric"):
    # Current weather endpoint
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": units}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def main():
    city = input("City (default: Tashkent): ").strip() or "Tashkent"
    try:
        data = get_current_weather(city)
    except requests.HTTPError as e:
        print("HTTP error:", e, file=sys.stderr)
        try:
            print("Response:", e.response.json())
        except Exception:
            pass
        return
    except Exception as e:
        print("Error fetching data:", e, file=sys.stderr)
        return

    # parse useful fields (from OpenWeather structure)
    name = data.get("name")
    main = data.get("main", {})
    weather_list = data.get("weather", [])
    wind = data.get("wind", {})

    temp = main.get("temp")
    feels_like = main.get("feels_like")
    humidity = main.get("humidity")
    pressure = main.get("pressure")
    description = weather_list[0].get("description") if weather_list else "N/A"
    wind_speed = wind.get("speed")

    print(f"Weather for {name}:")
    print(f"  Condition: {description}")
    print(f"  Temperature: {temp} °C (feels like {feels_like} °C)")
    print(f"  Humidity: {humidity}%")
    print(f"  Pressure: {pressure} hPa")
    print(f"  Wind speed: {wind_speed} m/s")

if __name__ == "__main__":
    main()

# books_manager.py
import json
from pathlib import Path
import argparse

DEFAULT_FILE = "books.json"

def load_books(path):
    p = Path(path)
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding="utf-8"))

def save_books(path, books):
    p = Path(path)
    p.write_text(json.dumps(books, indent=2, ensure_ascii=False), encoding="utf-8")

def list_books(books):
    if not books:
        print("No books.")
        return
    for i, b in enumerate(books, 1):
        print(f"{i}. {b.get('title','<no title>')} by {b.get('author','<no author>')} (id: {b.get('id','-')})")

def add_book(books):
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    year = input("Year (optional): ").strip()
    # generate simple id
    existing_ids = {b.get("id") for b in books}
    new_id = 1
    while new_id in existing_ids:
        new_id += 1
    book = {"id": new_id, "title": title, "author": author}
    if year:
        book["year"] = year
    books.append(book)
    print("Added:", book)

def find_book_by_id(books, bid):
    for b in books:
        if b.get("id") == bid:
            return b
    return None

def update_book(books):
    list_books(books)
    try:
        bid = int(input("Enter book id to update: ").strip())
    except:
        print("Invalid id")
        return
    b = find_book_by_id(books, bid)
    if not b:
        print("Book not found")
        return
    title = input(f"New title (enter to keep: {b.get('title')}): ").strip()
    author = input(f"New author (enter to keep: {b.get('author')}): ").strip()
    year = input(f"New year (enter to keep: {b.get('year','')}) : ").strip()
    if title: b["title"] = title
    if author: b["author"] = author
    if year: b["year"] = year
    print("Updated:", b)

def delete_book(books):
    list_books(books)
    try:
        bid = int(input("Enter book id to delete: ").strip())
    except:
        print("Invalid id")
        return
    b = find_book_by_id(books, bid)
    if not b:
        print("Book not found")
        return
    books.remove(b)
    print("Deleted:", b)

def main(path=DEFAULT_FILE):
    books = load_books(path)
    while True:
        print("\nCommands: list, add, update, delete, quit")
        cmd = input("> ").strip().lower()
        if cmd == "list":
            list_books(books)
        elif cmd == "add":
            add_book(books)
            save_books(path, books)
        elif cmd == "update":
            update_book(books)
            save_books(path, books)
        elif cmd == "delete":
            delete_book(books)
            save_books(path, books)
        elif cmd in ("quit", "exit"):
            save_books(path, books)
            print("Saved. Bye.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?", default=DEFAULT_FILE, help="Path to books.json")
    args = ap.parse_args()
    main(args.file)

# movie_recommender.py
import requests
import os
import random
import json

API_KEY = os.environ.get("OMDB_API_KEY")  # set your OMDb API key here
if not API_KEY:
    print("Please set OMDB_API_KEY environment variable.")
    raise SystemExit(1)

# A small seed list; expand or load from a file for better coverage
SEED_TITLES = [
    "The Shawshank Redemption", "Forrest Gump", "The Godfather",
    "Pulp Fiction", "The Dark Knight", "Inception", "Interstellar",
    "The Matrix", "Gladiator", "Spirited Away", "Parasite",
    "Avengers: Endgame", "The Silence of the Lambs", "La La Land",
    "Toy Story", "The Lion King", "Blade Runner 2049", "Mad Max: Fury Road"
]

def get_movie_details(title):
    url = "http://www.omdbapi.com/"
    params = {"apikey": API_KEY, "t": title, "r": "json"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    if data.get("Response", "False") == "True":
        return data
    return None

def recommend_by_genre(genre_query, seed_titles=SEED_TITLES):
    matches = []
    genre_query_l = genre_query.lower()
    for t in seed_titles:
        try:
            info = get_movie_details(t)
        except Exception:
            continue
        if not info:
            continue
        genres = info.get("Genre", "")
        # Genre string is like "Action, Adventure, Sci-Fi"
        if any(genre_query_l == g.strip().lower() for g in genres.split(",")):
            matches.append({
                "Title": info.get("Title"),
                "Year": info.get("Year"),
                "Genre": genres,
                "Plot": info.get("Plot"),
                "imdbID": info.get("imdbID")
            })
    if not matches:
        return None
    return random.choice(matches)

def main():
    g = input("Enter a movie genre (e.g. Drama, Action, Comedy): ").strip()
    rec = recommend_by_genre(g)
    if not rec:
        print("No recommendation found in the seed list for that genre.")
        print("Options: expand the seed list or use a different API (e.g. TMDB) that supports genre search server-side.")
        return
    print("Recommended movie:")
    print(f"{rec['Title']} ({rec['Year']})")
    print("Genres:", rec["Genre"])
    print("Plot:", rec["Plot"])
    print("IMDB:", f"https://www.imdb.com/title/{rec['imdbID']}/" if rec.get("imdbID") else "N/A")

if __name__ == "__main__":
    main()




