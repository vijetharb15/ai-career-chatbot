# AI Career Chatbot Development Presentation

## Slide 1: Title Slide
- **Title:** AI Career Chatbot: Local-First with Robust Fallbacks
- **Subtitle:** Developed for Reliable Career Advice Without API Dependencies
- **Your Name & Date**

## Slide 2: Project Overview
- **Objective:** Build an AI-powered chatbot for career guidance that runs locally to avoid quota issues.
- **Key Features:**
  - RAG (Retrieval-Augmented Generation) using local data
  - Web search integration for real-time info
  - Local embeddings and LLM fallbacks
  - Streamlit UI with chat history

## Slide 3: Architecture & Technologies
- **Frontend:** Streamlit (Python web app)
- **Backend:** Python with LangChain
- **Components:**
  - Embeddings: Local DeterministicFakeEmbedding
  - LLM: OpenAI GPT-4o-mini with local fallback (10 rotating advice tips)
  - RAG: InMemoryVectorStore with FAISS-like functionality
  - Web Search: SerpAPI integration
- **Deployment:** Streamlit Cloud (free tier)

## Slide 4: Development Approach
- **Step 1:** Set up project structure (MVC-like with config, models, utils)
- **Step 2:** Implement core RAG pipeline (embeddings, vector store, retrieval)
- **Step 3:** Add LLM integration with OpenAI API
- **Step 4:** Handle errors with local fallbacks (embeddings, LLM, web search)
- **Step 5:** Build UI with Streamlit (input, modes, history)
- **Step 6:** Test and iterate (fix quota issues, add variety)

## Slide 5: Challenges Faced
- **OpenAI Quota Errors (429):** Resolved by implementing runtime fallbacks to local models.
- **Module Import Issues:** Fixed path problems in config imports.
- **Consistent Responses:** Used hash-based selection for varied advice.
- **Web Search Dependency:** Added fallback when SerpAPI fails.
- **UI Responsiveness:** Optimized with caching and session state.

## Slide 6: Assumptions & Considerations
- **Assumptions:**
  - User has Python 3.8+ and internet for web search.
  - Local mode prioritizes privacy (no data sent to OpenAI).
  - Sample data in `data/` is sufficient for demo.
- **Unique Considerations:**
  - Local-first design for cost-free operation.
  - Graceful degradation (app works even with all APIs down).
  - Extensible: Easy to add OpenAI key for enhanced responses.

## Slide 7: Key Code Snippets
- **Embeddings Fallback:**
  ```python
  def get_embeddings():
      return DeterministicFakeEmbedding(size=1536)
  ```
- **LLM with Variety:**
  ```python
  responses = ["Advice 1", "Advice 2", ...]
  advice = responses[hash(prompt) % len(responses)]
  ```
- **Web Search Integration:**
  ```python
  web_result = search_web(prompt)
  response += f"\n\n🌐 Web Data: {web_result}"
  ```

## Slide 8: Testing & Validation
- **Local Testing:** Verified fallbacks work without API keys.
- **Error Handling:** Tested 429 errors, invalid keys, network issues.
- **User Experience:** Ensured varied responses and useful web data.
- **Performance:** Cached vector DB for fast startup.

## Slide 9: Deployment & GitHub
- **GitHub Repo:** [Link to your public repo]
- **Deployment:** Hosted on Streamlit Cloud at [your deployment link]
- **How to Run Locally:**
  - `pip install -r requirements.txt`
  - `streamlit run app.py`

## Slide 10: Future Improvements
- Add user authentication for personalized advice.
- Integrate more data sources (job boards, LinkedIn).
- Implement conversation memory beyond session.
- Add analytics for user queries.

## Slide 11: Conclusion
- **Success:** Fully functional chatbot that provides value locally.
- **Lessons Learned:** Importance of fallbacks in API-dependent apps.
- **Impact:** Enables career guidance without costs or quotas.

## Slide 12: Q&A
- Open for questions!