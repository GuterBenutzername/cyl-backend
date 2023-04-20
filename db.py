from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Assignment(Base):
    __tablename__ = "assignments"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    grade: Mapped[float]
    weight: Mapped[float]
    course: Mapped["Course"] = relationship(back_populates="assignments")
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"))


class Course(Base):
    __tablename__ = "courses"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    assignments: Mapped[list["Assignment"]] = relationship(back_populates="course")
    user: Mapped["User"] = relationship(back_populates="courses")
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    courses: Mapped[list["Course"]] = relationship(back_populates="user")
