from openai import OpenAI
from config.config import OPENAI_API_KEY
from utils.web_search import search_web


def generate_response(prompt):
    if not OPENAI_API_KEY:
        responses = [
            "Focus on building skills in high-demand areas like AI, data science, or software development. Network on LinkedIn and consider certifications to advance your career.",
            "Career transitions often require upskilling. Start by identifying your transferable skills and researching job markets. Consider online courses on platforms like Coursera or Udemy.",
            "For career growth, set clear goals, seek mentorship, and regularly update your resume. Don't forget to maintain work-life balance to avoid burnout.",
            "In today's job market, soft skills like communication and adaptability are crucial. Combine them with technical expertise for better opportunities.",
            "Explore internships or freelance projects to gain experience. Building a portfolio can significantly boost your job prospects in competitive fields.",
            "Consider specializing in emerging technologies such as blockchain or renewable energy. Attend industry conferences and join professional associations.",
            "Develop a personal brand by blogging, speaking at events, or contributing to open-source projects. This can open doors to new opportunities.",
            "Evaluate your current role for growth potential. If stagnation is an issue, look for lateral moves or promotions within your company.",
            "Invest in continuous learning through podcasts, webinars, and books. Knowledge in your field is key to staying relevant.",
            "Build a strong professional network. Relationships can lead to job offers, partnerships, and valuable advice."
        ]
        advice = responses[hash(prompt) % len(responses)]
        base_response = f"Based on your question '{prompt[:50]}...', here's career advice: {advice}"
        web_result = search_web(prompt)
        return f"{base_response}\n\n🌐 Additional info from web: {web_result}"

    client = OpenAI(api_key=OPENAI_API_KEY)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"[llm] OpenAI error: {e}; using local fallback.")
        responses = [
            "Focus on building skills in high-demand areas like AI, data science, or software development. Network on LinkedIn and consider certifications to advance your career.",
            "Career transitions often require upskilling. Start by identifying your transferable skills and researching job markets. Consider online courses on platforms like Coursera or Udemy.",
            "For career growth, set clear goals, seek mentorship, and regularly update your resume. Don't forget to maintain work-life balance to avoid burnout.",
            "In today's job market, soft skills like communication and adaptability are crucial. Combine them with technical expertise for better opportunities.",
            "Explore internships or freelance projects to gain experience. Building a portfolio can significantly boost your job prospects in competitive fields.",
            "Consider specializing in emerging technologies such as blockchain or renewable energy. Attend industry conferences and join professional associations.",
            "Develop a personal brand by blogging, speaking at events, or contributing to open-source projects. This can open doors to new opportunities.",
            "Evaluate your current role for growth potential. If stagnation is an issue, look for lateral moves or promotions within your company.",
            "Invest in continuous learning through podcasts, webinars, and books. Knowledge in your field is key to staying relevant.",
            "Build a strong professional network. Relationships can lead to job offers, partnerships, and valuable advice."
        ]
        advice = responses[hash(prompt) % len(responses)]
        base_response = f"Based on your question '{prompt[:50]}...', here's career advice: {advice}"
        web_result = search_web(prompt)
        return f"{base_response}\n\n🌐 Additional info from web: {web_result}"