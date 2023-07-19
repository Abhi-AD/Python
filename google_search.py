from googlesearch import search

def google_search(query):
    try:
        search_results = search(query, lang="en")
        return search_results
    except Exception as e:
        print("An error occurred:", str(e))
        return []

if __name__ == "__main__":
    print("*********************")
    user_query = input("Enter your search query: ")
    search_results = google_search(user_query)

    if search_results:
        print("------------------------")
        print("Search results:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result}")
    else:
        print("No results found.")
