#!/usr/bin/env python3
"""
Test script for AI Support Bot
This script tests the basic functionality without requiring a web interface.
"""

import os
import sys
import json
from app import AISupportBot, faq_collection

def test_faq_retrieval():
    """Test FAQ retrieval functionality"""
    print("🔍 Testing FAQ retrieval...")
    
    bot = AISupportBot()
    
    # Test queries
    test_queries = [
        "How do I reset my password?",
        "What are your business hours?",
        "How can I get a refund?",
        "I need help with my account"
    ]
    
    for query in test_queries:
        print(f"\n📝 Query: {query}")
        try:
            results = bot.get_relevant_faqs(query, n_results=2)
            if results and results['documents']:
                print("✅ Found relevant FAQs:")
                for i, doc in enumerate(results['documents'][0]):
                    print(f"   {i+1}. {doc[:100]}...")
            else:
                print("❌ No FAQs found")
        except Exception as e:
            print(f"❌ Error: {e}")

def test_faq_count():
    """Test if FAQs are loaded"""
    print("\n📊 Testing FAQ database...")
    try:
        count = faq_collection.count()
        print(f"✅ FAQ count: {count}")
        
        if count > 0:
            print("✅ Sample FAQs are loaded")
        else:
            print("❌ No FAQs found in database")
    except Exception as e:
        print(f"❌ Error accessing FAQ database: {e}")

def test_openai_connection():
    """Test OpenAI API connection"""
    print("\n🤖 Testing OpenAI connection...")
    
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ OPENAI_API_KEY not set")
        return False
    
    try:
        import openai
        # Simple test request
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello, this is a test."}],
            max_tokens=10
        )
        print("✅ OpenAI API connection successful")
        return True
    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 AI Support Bot Test Suite")
    print("=" * 40)
    
    # Test FAQ database
    test_faq_count()
    
    # Test FAQ retrieval
    test_faq_retrieval()
    
    # Test OpenAI connection
    openai_works = test_openai_connection()
    
    print("\n" + "=" * 40)
    if openai_works:
        print("🎉 All tests completed! The bot should work correctly.")
        print("💡 Run 'python app.py' to start the web server")
    else:
        print("⚠️  Some tests failed. Please check your OpenAI API key and try again.")

if __name__ == "__main__":
    main()



