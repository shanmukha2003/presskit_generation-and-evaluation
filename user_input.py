def get_user_input():
    """Collects user input for press kit generation."""
    print("\n[User Input Stage]")
    
    # Collect company information
    company_name = input("Enter Company Name: ")
    
    # Collect press kit generation topic
    press_kit_topic = input("Enter Press Kit Topic: ")
    target_media = input("Enter Target Media (e.g., Tech News, Business Magazines): ")
    tone = input("Enter Preferred Tone (Professional/Creative/Formal): ")
    
    # Display summary for confirmation
    print("\n[User Input Summary]")
    print(f"Company Name: {company_name}")
    print(f"Press Kit Topic: {press_kit_topic}")
    print(f"Target Media: {target_media}")
    print(f"Tone: {tone}")
    
    confirm = input("\nIs the above information correct? (Y/N): ")
    if confirm.lower() != 'y':
        print("Restarting input collection...")
        return get_user_input()
    
    return company_name, press_kit_topic, target_media, tone
