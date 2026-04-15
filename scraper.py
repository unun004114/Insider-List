import os
import requests
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

def fetch_data():
    # 예시: 특정 RSS나 공개 API (여기서는 예시 데이터로 작동 확인)
    # 실제 운영 시 이 부분에 원하는 사이트의 스크래핑 로직을 넣습니다.
    return [
        {"title": "[Project] Premium Design Work", "link": "https://example.com/1", "category": "Design"},
        {"title": "[Job] Senior Scripting Expert", "link": "https://example.com/2", "category": "Dev"}
    ]

def main():
    items = fetch_data()
    for item in items:
        supabase.table("posts").upsert(item, on_conflict="link").execute()
    
    # 24시간 지난 공고는 무료로 전환
    supabase.rpc('unlock_posts').execute() # 이 함수는 나중에 DB에 등록

if __name__ == "__main__":
    main()
