from requests import get
from bs4 import BeautifulSoup



def reddit_scrapper(query):
    url = f'https://www.reddit.com/search/?q={query}'
    soup = BeautifulSoup(get(url).text,'html.parser')

    main_div = soup.find('div',{'class':'_2mO8vClBdPxiJ30y_C6od2'})
    posted_date = []
    post_urls = []
    post_text = []
    image_urls = []

    #Getting Posted Date
    all_posted_dates = main_div.find_all('span',{'data-testid':'post_timestamp'})
    [posted_date.append(pd.text) for pd in all_posted_dates]


    #Getting Posted Url
    all_posts = main_div.find_all('div',{'data-testid':'post-container'})
    for post in all_posts:
        post_url = post.find_all('a')[0]
        post_urls.append('https://reddit.com'+post_url.attrs['href'])


    #Getting Post text
    texts = main_div.find_all('h3',{'class':'_eYtD2XCVieq6emjKBH3m'})
    [post_text.append(t.text) for t in texts]
    print(post_text)


    #Getting Image Url
    img_url = main_div.find_all('a',{'rel':'noopener nofollow ugc'})
    [image_urls.append(iu.attrs['href']) for iu in img_url]
    



    for p in zip(post_text,post_urls,image_urls,posted_date):
        print(f"\n\nPost Image {p[2]}\nPost Text : {p[0]}\n\nPosted Date : {p[3]}\n\nPost Url : {p[1]}\n\n\n")


if __name__ == '__main__':
    q = input("What would you like to search for ? ")
    reddit_scrapper(q)