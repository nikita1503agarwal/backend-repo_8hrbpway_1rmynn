"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (retain for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# ---------------------------------------------
# Lead capture schema for B2B SaaS landing page
# Collection name: "lead"
# ---------------------------------------------
class Lead(BaseModel):
    company: str = Field(..., min_length=2, description="Company name")
    full_name: str = Field(..., min_length=2, description="Contact person full name")
    email: EmailStr = Field(..., description="Business email")
    phone: Optional[str] = Field(None, description="Phone number")
    employees: Optional[str] = Field(
        None,
        description="Company size segment (e.g., 1-10, 11-50, 51-200, 200+)"
    )
    plan: Optional[str] = Field(None, description="Selected plan at submission time")
    message: Optional[str] = Field(None, description="Additional context or goals")
    source: Optional[str] = Field(None, description="UTM/source for CRO tracking")
