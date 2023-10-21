import pandas as pd

# 상대경로가 안될시 여기에 절대경로를 적어주세요
dir = '/Users/owo/HOUSE/@Code/-Study/@SCHOOL/data/book.csv'

try:
    books_df = pd.read_csv('data/book.csv', encoding='cp949')
except:
    try:
        books_df = pd.read_csv('book.csv', encoding='cp949')
    except:
        books_df = pd.read_csv(dir, encoding='cp949')

# 가장 긴 제목과 짧은 제목의 책 찾기
longest_title_length = books_df['도 서 명'].str.len().max()
shortest_title_length = books_df['도 서 명'].str.len().min()

longest_titles = books_df[books_df['도 서 명'].str.len(
) == longest_title_length]['도 서 명'].tolist()
shortest_titles = books_df[books_df['도 서 명'].str.len(
) == shortest_title_length]['도 서 명'].tolist()

# 저자 수 파악
unique_authors = books_df['저자명'].nunique()

# 가장 많은 책을 쓴 저자 찾기
author_counts = books_df['저자명'].value_counts()
max_books_written = author_counts.max()
most_prolific_authors = author_counts[author_counts ==
                                      max_books_written].index.tolist()

# 가장 많은 책을 쓴 저자의 책 목록
books_by_most_prolific = books_df[books_df['저자명'].isin(
    most_prolific_authors)][['저자명', '도 서 명']]

# 가장 많은 책을 출판한 상위 5개 출판사
top_publishers = books_df['출판사'].value_counts().head(5)

# 분야별 가장 많은 책을 출판한 출판사 찾기
categories = ['역사', '철학사상']
top_publishers_by_category = {}
for category in categories:
    category_publishers = books_df[books_df['장르']
                                   == category]['출판사'].value_counts()
    max_books_in_category = category_publishers.max()
    top_publishers_for_category = category_publishers[category_publishers ==
                                                      max_books_in_category].index.tolist()
    top_publishers_by_category[category] = top_publishers_for_category

# 결과 출력
# 가장 긴 제목과 짧은 제목의 책
if len(longest_titles) > 1:
    print(
        f"가장 긴 제목의 책이 {len(longest_titles)}권 있습니다: {', '.join(longest_titles)}")
else:
    print(f"가장 긴 제목의 책: {longest_titles[0]}")

if len(shortest_titles) > 1:
    print(
        f"가장 짧은 제목의 책이 {len(shortest_titles)}권 있습니다: {', '.join(shortest_titles)}")
else:
    print(f"가장 짧은 제목의 책: {shortest_titles[0]}")

# 저자 수
print(f"\n도서의 저자는 총 {unique_authors}명입니다.")

# 가장 많은 책을 쓴 저자와 그의 책 제목
print("\n가장 많은 책을 쓴 저자와 그의 책 제목:")
for author in most_prolific_authors:
    author_books = books_by_most_prolific[books_by_most_prolific['저자명']
                                          == author]['도 서 명'].tolist()
    print(f"저자 {author}")
    for book in author_books:
        print(f"   - {book}")

# 상위 5개 출판사
print("\n최대 책을 출판한 5개 출판사:")
for publisher, count in top_publishers.items():
    print(f"{publisher}")

# 분야별 출판사
print("\n분야별 가장 많은 책을 출판한 출판사:")
for category, publishers in top_publishers_by_category.items():
    print(f"{category} 분야 : {', '.join(publishers)}")
