"""
Optimized chat system with optional LLM and fast fallback responses.
"""

import streamlit as st

# Fast FAQ-style responses (no LLM needed)
FAQ_RESPONSES = {
    "substitute": """Here are common ingredient substitutions:
    
🥚 **Eggs**: Use flax eggs (1 tbsp ground flaxseed + 3 tbsp water per egg), applesauce, or mashed banana
🥛 **Milk**: Try almond milk, oat milk, soy milk, or coconut milk
🧈 **Butter**: Use coconut oil, olive oil, or vegan butter
🍖 **Chicken**: Substitute with tofu, tempeh, or chickpeas
🐟 **Fish**: Try tofu, mushrooms, or plant-based alternatives
🧀 **Cheese**: Use nutritional yeast, cashew cheese, or vegan cheese
🍞 **Bread**: Try lettuce wraps, rice paper, or gluten-free bread
🍝 **Pasta**: Use zucchini noodles, shirataki noodles, or whole wheat pasta""",
    
    "allergy": """For common allergies, here are safe alternatives:

🥜 **Nut Allergies**: Use sunflower seed butter, tahini, or soy nut butter
🌾 **Gluten**: Choose rice, quinoa, buckwheat, or certified gluten-free products
🥛 **Dairy**: Opt for coconut, almond, oat, or soy-based alternatives
🦐 **Shellfish**: Avoid all shellfish; use plant-based proteins instead
🥚 **Eggs**: Use commercial egg replacers or flax/chia eggs

Always read labels carefully and consult with a healthcare provider for severe allergies.""",
    
    "cooking": """Quick cooking tips:

⏱️ **Save Time**: Prep ingredients in advance, use a pressure cooker, or batch cook
🔥 **Better Flavor**: Season in layers, taste as you go, and let meat rest before cutting
🥘 **Texture**: Don't overcrowd the pan, use high heat for searing, low for braising
❄️ **Storage**: Cool food before refrigerating, use airtight containers, label with dates
♻️ **Reduce Waste**: Save vegetable scraps for stock, freeze herbs in oil, repurpose leftovers""",
    
    "nutrition": """Nutrition basics:

🥗 **Balanced Plate**: 1/2 vegetables, 1/4 protein, 1/4 whole grains
💪 **Protein**: Aim for 0.8g per kg body weight (more if active)
🥤 **Hydration**: Drink 8-10 glasses of water daily
🍎 **Fiber**: Get 25-30g daily from fruits, vegetables, and whole grains
🥑 **Healthy Fats**: Include nuts, seeds, avocado, and olive oil
🍬 **Sugar**: Limit added sugars to less than 10% of daily calories""",
    
    "meal_prep": """Meal prep strategies:

📅 **Plan Ahead**: Choose 3-4 recipes for the week
🛒 **Smart Shopping**: Make a list, shop once, buy in bulk
🍱 **Batch Cook**: Cook grains, proteins, and veggies in large batches
📦 **Portion Control**: Use containers to pre-portion meals
❄️ **Freeze Smart**: Label everything, freeze flat for easy storage
🔄 **Mix & Match**: Prepare versatile ingredients that work in multiple dishes""",
    
    "budget": """Eating healthy on a budget:

💰 **Buy Smart**: Choose seasonal produce, buy frozen vegetables, use store brands
🌾 **Protein Sources**: Eggs, beans, lentils, and canned fish are affordable
🥫 **Pantry Staples**: Stock rice, pasta, canned tomatoes, and dried beans
🥬 **Reduce Waste**: Use leftovers creatively, freeze extras, plan portions
🛍️ **Shop Sales**: Buy in bulk when on sale, use coupons, compare unit prices"""
}

def get_quick_response(user_question: str) -> str:
    """
    Provide fast FAQ-style responses based on keywords.
    """
    question_lower = user_question.lower()
    
    # Check for keywords and return relevant FAQ
    if any(word in question_lower for word in ['substitute', 'replace', 'instead', 'swap', 'alternative']):
        return FAQ_RESPONSES['substitute']
    elif any(word in question_lower for word in ['allergy', 'allergic', 'intolerance', 'sensitive']):
        return FAQ_RESPONSES['allergy']
    elif any(word in question_lower for word in ['cook', 'prepare', 'recipe', 'how to', 'tips']):
        return FAQ_RESPONSES['cooking']
    elif any(word in question_lower for word in ['nutrition', 'healthy', 'calories', 'protein', 'vitamins']):
        return FAQ_RESPONSES['nutrition']
    elif any(word in question_lower for word in ['meal prep', 'prepare ahead', 'batch', 'planning']):
        return FAQ_RESPONSES['meal_prep']
    elif any(word in question_lower for word in ['budget', 'cheap', 'affordable', 'save money', 'cost']):
        return FAQ_RESPONSES['budget']
    else:
        return """I can help with:
        
• 🔄 **Ingredient substitutions** - Ask about swapping ingredients
• 🚫 **Allergy alternatives** - Get safe food alternatives  
• 👨‍🍳 **Cooking tips** - Learn cooking techniques
• 🥗 **Nutrition advice** - Understand nutritional basics
• 📅 **Meal prep** - Plan and prepare meals efficiently
• 💰 **Budget tips** - Eat healthy affordably

Try asking a more specific question, or enable AI Chat for personalized responses!"""


def generate_chat_answer(context_text: str, history_text: str, user_message: str, use_ai: bool = False) -> str:
    """
    Generate a chat response. Uses fast FAQ by default, or LLM if enabled.
    
    Args:
        context_text: Text describing current recommended recipes
        history_text: Previous chat history
        user_message: The user's question
        use_ai: If True, use LLM (slow). If False, use fast FAQ responses.
        
    Returns:
        The assistant's reply
    """
    if not use_ai:
        # Fast FAQ-based response
        return get_quick_response(user_message)
    
    # LLM-based response (slow but more personalized)
    try:
        # Import here to avoid loading if not needed
        from llm_chat import generate_chat_answer as llm_generate
        return llm_generate(context_text, history_text, user_message)
    except Exception as e:
        return f"⚠️ AI chat error: {str(e)}. Try using Quick Response mode instead."
