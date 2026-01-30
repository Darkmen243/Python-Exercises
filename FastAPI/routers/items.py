'''
Create /items API:

name (str)

price (float, >0)

quantity (int, >=0)

Implement:

Create

Update

Delete

List
'''

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import Float, String, create_engine, Integer
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Session,
    Mapped,
    mapped_column,
)
from pydantic import BaseModel, Field

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)



Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


class ItemUpdate(BaseModel):
    name: str
    description: str | None = None
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


class ItemRead(BaseModel):
    id: int
    name: str
    description: str | None = None
    price : float 
    quantity : int

    class Config:
        from_attributes = True  


router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(
    item_in: ItemCreate,
    db: Session = Depends(get_db),
):
    if item_in.price>0 and item_in.quantity>0:
        item = Item(
            name=item_in.name,
            description=item_in.description,
        )
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quantity or Price is invalid for this item."
        )


@router.get("/{item_id}", response_model=ItemRead)
def read_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )

    return item


@router.put("/{item_id}", response_model=ItemRead)
def update_item(
    item_id: int,
    item_in: ItemUpdate,
    db: Session = Depends(get_db),
):
    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )

    item.name = item_in.name
    item.description = item_in.description

    db.commit()
    db.refresh(item)
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )

    db.delete(item)
    db.commit()