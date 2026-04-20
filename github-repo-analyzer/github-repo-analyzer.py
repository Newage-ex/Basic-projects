import requests 

username = input("GitHub username: ") 
url = f"https://api.github.com/users/{username}/repos" 

response = requests.get(url)
data = response.json()

total_repos = 0 
max_stars = 0 
top_repo = ""
total_stars = 0

for repo in data: 
    stars = repo["stargazers_count"]
    
    print(repo["name"], stars)
    
    total_repos += 1
    total_stars += stars

    if stars > max_stars:
        max_stars = stars
        top_repo = repo["name"]

print("\n--- Summary ---")

if total_repos == 0:
    print("No repositories found.")
else:
    avg_stars = total_stars / total_repos

    print(f"Total repos: {total_repos}")
    print(f"Top repo: {top_repo} ({max_stars})")
    print(f"Average stars: {avg_stars:.2f}")