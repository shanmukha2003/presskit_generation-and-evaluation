import llama_cpp
from config import LLAMA_MODEL_PATH
from user_input import get_user_input
from news_fetcher import fetch_latest_news
from quality_review import evaluate_press_kit  # Import the quality review function

def load_model():
    """Loads the LLaMA 3 model from the specified GGUF file."""
    print("\n[Model Loading]")
    try:
        llm = llama_cpp.Llama(model_path=LLAMA_MODEL_PATH)
        print("✅ Model loaded successfully!")
        return llm
    except Exception as e:
        print(f"⚠ Error loading model: {e}")
        return None

def generate_press_kit(model, company_name, press_kit_topic, target_media, tone, supplementary_data):
    """Generates a press kit draft using LLaMA 3."""
    
    while True:
        print("\n[Generating Press Kit Draft ⚡]")

        prompt = (
            f"Generate a detailed {tone} press release for {company_name}. "
            f"Topic: {press_kit_topic}. Target media: {target_media}.\n"
            f"Here is some supplementary information:\n{supplementary_data}\n"
            f"Structure the output as follows:\n"
            f"1. **Company Overview**\n"
            f"2. **Press Release**\n"
            f"3. **PR Message**\n"
            f"4. **Email Draft**\n"
            f"Ensure that every section is fully generated and complete. The output must be structured, formatted cleanly, and include all details as expected."
        )

        try:
            response = model(
                prompt,
                max_tokens=8192,
                temperature=0.7,
                top_k=50,
                repeat_penalty=1.1,
            )

            press_kit_draft = response.get("choices", [{}])[0].get("text", "").strip()

            print("\n✅ [Draft Preview Completed]\n", press_kit_draft)

            confirm = input("\nProceed with this draft? (Y/N/Modify): ").strip().lower()

            if confirm == "y":
                print("\n✅ Final Press Kit Approved!\n")
                print("\n---- Clean Final Draft ----\n")
                print(press_kit_draft)
                
                # 🔥 Run quality review AFTER final approval
                print("\n🔍 Running AI-Based Quality Review...")
                review_result = evaluate_press_kit(press_kit_draft)

                print("\n📊 [Quality Review Report]")
                for key, value in review_result.items():
                    print(f"{key}: {value}")

                return press_kit_draft

            elif confirm == "modify":
                print("\n🔄 Enter your modifications:")
                user_feedback = input("Describe changes (e.g., 'Make it more formal', 'Improve SEO', etc.): ").strip()

                print("\n🔄 Regenerating the press kit with your modifications...\n")

                # Update the prompt with user feedback
                prompt += f"\nModify the draft based on the following user recommendations: {user_feedback}"

            elif confirm == "n":
                print("\n❌ Draft Rejected. Exiting...\n")
                return None
            else:
                print("\n⚠ Invalid input. Please enter Y, N, or Modify.")

        except Exception as e:
            print(f"\n⚠ Error generating press kit: {e}")
            return None

if __name__ == "__main__":
    model = load_model()
    if model:
        print("LLaMA 3 is ready for text generation.")
        company_name, press_kit_topic, target_media, tone = get_user_input()
        supplementary_data = fetch_latest_news(company_name)
        
        confirm = input("\nProceed with generating the press kit? (Y/N): ")
        if confirm.lower() == 'y':
            press_kit = generate_press_kit(model, company_name, press_kit_topic, target_media, tone, supplementary_data)
            if not press_kit:
                print("Please modify the inputs and try again.")
        else:
            print("Press kit generation canceled.") 
