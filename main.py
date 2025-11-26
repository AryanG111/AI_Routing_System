from workflow import AIWorkflow

if __name__ == "__main__":
    system = AIWorkflow()
    
    # Test Query
    user_input = "How can we build an AI app that reduces food waste and makes money?"
    
    result = system.process_query(user_input)
    
    print("\n" + "="*50)
    print("FINAL UNIFIED ANSWER")
    print("="*50)
    print(result)   