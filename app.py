import openai
import streamlit as st

# Set the page configuration first
st.set_page_config(page_title="Trợ lý AI báo cáo dữ liệu", layout="wide")

# Set your OpenAI API key
openai.api_key = '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'

# Initialize session state variables
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Helper function to safely load file content
def load_file_content(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except Exception as e:
        st.error(f"Lỗi khi đọc file {file_path}: {e}")
        return ""

# Load dataset-related information
dataset_text = load_file_content("dataset_info.txt")
extra_info = load_file_content("extra_info.txt")
extra_info_2 = load_file_content("extra_info_2.txt")
density = load_file_content("density.txt")
openai_insights = load_file_content("openai_insights.txt")
openai_insights_2 = load_file_content("openai_insights_2.txt")
openai_summary = load_file_content("openai_summary.txt")

# Function to interact with OpenAI API
def generate_openai_response(prompt, model="gpt-4o-mini", max_tokens=1500):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "Bạn là một trợ lý thông minh, có khả năng trả lời các câu hỏi liên quan đến một bộ dữ liệu lớn."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Lỗi khi gọi API OpenAI: {e}"

# Process user query with dataset context
def process_user_query(query):
    system_prompt = (
        f"""
        Bạn là một trợ lý thông minh với khả năng trả lời các câu hỏi phức tạp liên quan đến bộ dữ liệu lớn và phân tích sâu sắc. Bạn có khả năng giúp người dùng hiểu rõ hơn về các thông tin và các phân tích có sẵn, cũng như hỗ trợ họ đưa ra các quyết định chính xác và hợp lý dựa trên dữ liệu.

        **Thông tin về bộ dữ liệu**:
        {dataset_text}

        **Nhận xét từ con người**:
        {extra_info}
        {extra_info_2}

        **Mật độ và phân phối dữ liệu**:
        {density}

        **Phân tích và nhận xét từ OpenAI**:
        {openai_insights}
        {openai_insights_2}

        **Tóm tắt tổng quan**:
        {openai_summary}

        **Nhiệm vụ của bạn**:
        - Xử lý và chọn lọc các thông tin quan trọng, đặc biệt chú trọng đến những yếu tố có tính trùng lặp cao và bảo đảm tính chính xác trong các phân tích.
        - Cung cấp các dự đoán hoặc giải thích dựa trên dữ liệu có sẵn và kết nối các phân tích với các tình huống thực tế. Đảm bảo rằng các dự đoán này dễ hiểu và có thể giúp người dùng hình dung rõ ràng về kết quả có thể xảy ra.
        - Phân tích và kết nối các yếu tố dữ liệu để tạo ra những nhận xét có chiều sâu và hữu ích cho người dùng. Đưa ra các nhận xét bổ sung nếu nhận thấy rằng người dùng có thể chưa nhận ra một mối liên hệ quan trọng nào đó trong dữ liệu.
        - Khi trả lời câu hỏi, hãy đảm bảo rằng câu trả lời của bạn rõ ràng, dễ hiểu và mạch lạc. Đặc biệt chú trọng đến việc giải quyết các câu hỏi phức tạp hoặc mơ hồ bằng cách cung cấp các giải thích chi tiết và dễ tiếp cận.
        - Nếu câu hỏi có sự mơ hồ hoặc không rõ ràng, hãy yêu cầu người dùng cung cấp thêm thông tin và làm rõ các yêu cầu, hoặc đề xuất các giải pháp khả thi mà họ có thể tham khảo để đạt được câu trả lời chính xác hơn.

        **Câu hỏi từ người dùng**: {query}

        Hãy trả lời một cách chi tiết, rõ ràng và chính xác bằng Tiếng Việt. Đảm bảo rằng câu trả lời của bạn không chỉ đầy đủ mà còn có tính linh hoạt, giúp người dùng không chỉ trả lời câu hỏi mà còn khám phá thêm thông tin có giá trị từ bộ dữ liệu.
        """
    )
    return generate_openai_response(system_prompt)


# Streamlit UI components
st.title("Trợ lý AI báo cáo dữ liệu")
st.markdown("Hãy đặt câu hỏi liên quan đến bộ dữ liệu để nhận các phân tích chi tiết.")

# Display previous chat messages from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input for the query
user_input = st.chat_input("Hãy đặt câu hỏi về bộ dữ liệu:")
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.chat_message("assistant"):
        response = process_user_query(user_input)
        st.markdown(response)
    
    # Append assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
