from sqlalchemy.orm import Session

from api import models
from api.routers.auth_helper import PasswordHasher
from tests.testutils.db.factories import UserFactory


def create_users(db: Session):
    password = "password"
    password_hashed = PasswordHasher().hash_password(password)
    user = UserFactory(username="test_user", email="testuser@example.com", password_hashed=password_hashed)
    db.add(user)
    db.commit()
