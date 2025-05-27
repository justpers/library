#테스트 코드 (18점)
import pytest
from django.contrib.auth.models import User
from library.models import Book, BorrowHistory
from library.services.book_service import get_borrow_history_for_book
from library.exceptions import BookHasNoBorrowHistory

@pytest.mark.django_db
def test_get_borrow_history_for_book_success():
    # Given
    user = User.objects.create_user(username='testuser', password='1234')
    book = Book.objects.create(title='Test Book', author='Tester', isbn='1234567890123')
    BorrowHistory.objects.create(book=book, user=user)

    # When
    histories = get_borrow_history_for_book(book)

    # Then
    assert histories.count() == 1
    assert histories.first().user == user

@pytest.mark.django_db
def test_get_borrow_history_for_book_no_history():
    # Given
    book = Book.objects.create(title='Empty Book', author='Nobody', isbn='9999999999999')

    # When & Then
    with pytest.raises(BookHasNoBorrowHistory) as exc_info:
        get_borrow_history_for_book(book)

    assert "'Empty Book' 도서에는 대출 이력이 없습니다." == str(exc_info.value)

## 테스트 코드 예시 (12점)
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testlibrary.settings")
#
# import django
# django.setup()
#
# import pytest
# from library.models import Book
# from library.services.book_service import get_book_by_id
# from library.exceptions import BookNotFound
# import uuid
#
# @pytest.mark.django_db
# def test_get_book_by_id_success():
#     # Given
#     book = Book.objects.create(title='Test Book', author='Tester', isbn=str(uuid.uuid4().int)[:13])
#
#     # When
#     result = get_book_by_id(book.id)
#
#     # Then
#     assert result == book
#     assert result.title == 'Test Book'
#
#
# @pytest.mark.django_db
# def test_get_book_by_id_not_found():
#     # When & Then
#     with pytest.raises(BookNotFound) as exc_info:
#         get_book_by_id(99999)
#
#     assert "ID 99999에 해당하는 책이 없습니다." in str(exc_info.value)