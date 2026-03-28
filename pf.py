# ==============================
# Movie Recommendation System - Section A & B(c)
# ==============================

class Movie:
    def __init__(self, movie_id, title, genre, year):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.year = year
        self.ratings = []
        self.view_count = 0

    def get_average_rating(self):
        if not self.ratings:
            return 0.0
        return sum(self.ratings) / len(self.ratings)

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.watch_history = []
        self.ratings = {}

    def add_to_history(self, movie):
        if movie not in self.watch_history:
            self.watch_history.append(movie)
            movie.view_count += 1

    def rate_movie(self, movie, score):
        self.ratings[movie.movie_id] = score
        movie.ratings.append(score)
        self.add_to_history(movie)

# ==============================
# Section B(c) - Admin Console
# ==============================
def admin_console(system, users, admin_key="0390769"):
    """
    Admin console with secure login.
    Supports movie management and user engagement analytics.
    """
    key = input("Enter admin login key: ").strip()
    if key != admin_key:
        print("Access denied.")
        return

    print("\n===== Admin Console =====")

    while True:
        print("\n1. Add Movie")
        print("2. Edit Movie")
        print("3. Remove Movie")
        print("4. Engagement Analytics")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        # Add new movie
        if choice == "1":
            title = input("Movie title: ").strip()
            genre = input("Genre: ").strip()
            try:
                year = int(input("Year: ").strip())
                movie_id = len(system.movie_database) + 1
                new_movie = Movie(movie_id, title, genre, year)
                system.movie_database.append(new_movie)
                print(f"Added: {title} ({genre}, {year})")
            except:
                print("Invalid year. Movie not added.")

        # Edit movie
        elif choice == "2":
            print("Movies in database:")
            for i, m in enumerate(system.movie_database):
                print(f"{i+1}. {m.title} ({m.genre}, {m.year})")
            try:
                idx = int(input("Enter movie number to edit: ")) - 1
                if 0 <= idx < len(system.movie_database):
                    movie = system.movie_database[idx]
                    new_title = input(f"New title ({movie.title}): ").strip() or movie.title
                    new_genre = input(f"New genre ({movie.genre}): ").strip() or movie.genre
                    new_year_input = input(f"New year ({movie.year}): ").strip()
                    new_year = int(new_year_input) if new_year_input else movie.year
                    movie.title = new_title
                    movie.genre = new_genre
                    movie.year = new_year
                    print(f"Updated: {movie.title}")
                else:
                    print("Invalid selection.")
            except:
                print("Invalid input.")

        # Remove movie
        elif choice == "3":
            print("Movies in database:")
            for i, m in enumerate(system.movie_database):
                print(f"{i+1}. {m.title}")
            try:
                idx = int(input("Enter movie number to remove: ")) - 1
                if 0 <= idx < len(system.movie_database):
                    removed = system.movie_database.pop(idx)
                    print(f"Removed: {removed.title}")
                else:
                    print("Invalid selection.")
            except:
                print("Invalid input.")

        # Engagement analytics
        elif choice == "4":
            print("\n--- Engagement Analytics ---")

            watch_count = {}
            for u in users:
                for m in u.watch_history:
                    watch_count[m] = watch_count.get(m, 0) + 1

            # Most watched movies
            sorted_watch = sorted(watch_count.items(), key=lambda x: x[1], reverse=True)
            print("\nMost Watched Movies:")
            for m, count in sorted_watch[:3]:
                print(f"- {m.title}: {count} views")

            # Top active users
            top_users = sorted(users, key=lambda u: len(u.watch_history), reverse=True)
            print("\nTop Active Users:")
            for u in top_users[:3]:
                print(f"- {u.username}: {len(u.watch_history)} movies")

            # Trending movies
            print("\nTrending Movies (Score: Rating × Views):")
            for m, count in sorted_watch[:3]:
                score = m.get_average_rating() * count
                print(f"- {m.title}: Score {score:.1f}")

        elif choice == "5":
            print("Exiting Admin Console...")
            break

        else:
            print("Invalid choice. Try again.")

# ==============================
# 必须添加的初始化代码（现在才不会报错）
# ==============================
# 1. 初始化系统对象
system = type('obj', (object,), {'movie_database': []})()

# 2. 添加一些电影
movie1 = Movie(1, "The Matrix", "Action", 1999)
movie2 = Movie(2, "Titanic", "Romance", 1997)
movie3 = Movie(3, "Inception", "Action", 2010)
system.movie_database.extend([movie1, movie2, movie3])

# 3. 创建用户 u1
u1 = User(1, "StudentUser")

# 4. 让 u1 先评一些分（为了后面截图有数据）
u1.rate_movie(movie1, 5)
u1.rate_movie(movie2, 4)
u1.rate_movie(movie3, 5)

# 5. 用户列表（给管理员后台用）
users = [u1]

# ==============================
# 启动管理员控制台（现在绝对不会报错）
# ==============================
admin_console(system, users)