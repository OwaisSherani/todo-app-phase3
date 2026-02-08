#!/usr/bin/env python3
"""
Debug script to identify the exact issue
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("Step 1: Testing basic FastAPI import...")
try:
    from fastapi import FastAPI
    print("[OK] FastAPI imported successfully")
except Exception as e:
    print(f"[ERROR] FastAPI import failed: {e}")
    sys.exit(1)

print("\nStep 2: Testing SQLModel import...")
try:
    from sqlmodel import SQLModel
    print("[OK] SQLModel imported successfully")
except Exception as e:
    print(f"[ERROR] SQLModel import failed: {e}")
    sys.exit(1)

print("\nStep 3: Testing models import...")
try:
    from models import Task, TaskCreate, TaskUpdate, TaskRead
    print("[OK] Models imported successfully")
except Exception as e:
    print(f"[ERROR] Models import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\nStep 4: Testing database connection...")
try:
    from database import engine
    print("[OK] Database engine created successfully")
except Exception as e:
    print(f"[ERROR] Database connection failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\nStep 5: Testing dependencies import...")
try:
    from dependencies import get_db_session
    print("[OK] Dependencies imported successfully")
except Exception as e:
    print(f"[ERROR] Dependencies import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\nStep 6: Testing auth import...")
try:
    from auth import get_current_user_id
    print("[OK] Auth module imported successfully")
except Exception as e:
    print(f"[ERROR] Auth module import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\nStep 7: Testing router import...")
try:
    import routers.tasks
    print("[OK] Router imported successfully")
except Exception as e:
    print(f"[ERROR] Router import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\nStep 8: Creating basic app without lifespan...")
try:
    app = FastAPI(title="Test API", version="1.0.0")
    
    @app.get("/")
    def read_root():
        return {"message": "Test API is running"}
    
    print("[OK] Basic app created successfully")
except Exception as e:
    print(f"[ERROR] Basic app creation failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\nStep 9: Creating app with router...")
try:
    app_with_router = FastAPI(title="Test API with Router", version="1.0.0")
    import routers.tasks
    app_with_router.include_router(routers.tasks.router, prefix="/api/{user_id}", tags=["tasks"])
    
    @app_with_router.get("/")
    def read_root():
        return {"message": "Test API with Router is running"}
    
    print("[OK] App with router created successfully")
except Exception as e:
    print(f"[ERROR] App with router creation failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\nAll tests passed! The issue might be with the lifespan function or database initialization.")