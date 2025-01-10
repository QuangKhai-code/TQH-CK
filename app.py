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

        *Thông tin về bộ dữ liệu*:
        {dataset_text}

        *Nhận xét từ con người*:
        {extra_info}
        {extra_info_2}

        *Mật độ và phân phối dữ liệu*:
        {density}

        *Phân tích và nhận xét từ OpenAI*:
        {openai_insights}
        {openai_insights_2}

        *Tóm tắt tổng quan*:
        {openai_summary}

        *Nhiệm vụ của bạn*:
        - Xử lý và chọn lọc các thông tin quan trọng, đặc biệt chú trọng đến những yếu tố có tính trùng lặp cao và bảo đảm tính chính xác trong các phân tích.
        - Cung cấp các dự đoán hoặc giải thích dựa trên dữ liệu có sẵn và kết nối các phân tích với các tình huống thực tế. Đảm bảo rằng các dự đoán này dễ hiểu và có thể giúp người dùng hình dung rõ ràng về kết quả có thể xảy ra.
        - Phân tích và kết nối các yếu tố dữ liệu để tạo ra những nhận xét có chiều sâu và hữu ích cho người dùng. Đưa ra các nhận xét bổ sung nếu nhận thấy rằng người dùng có thể chưa nhận ra một mối liên hệ quan trọng nào đó trong dữ liệu.
        - Khi trả lời câu hỏi, hãy đảm bảo rằng câu trả lời của bạn rõ ràng, dễ hiểu và mạch lạc. Đặc biệt chú trọng đến việc giải quyết các câu hỏi phức tạp hoặc mơ hồ bằng cách cung cấp các giải thích chi tiết và dễ tiếp cận.
        - Nếu câu hỏi có sự mơ hồ hoặc không rõ ràng, hãy yêu cầu người dùng cung cấp thêm thông tin và làm rõ các yêu cầu, hoặc đề xuất các giải pháp khả thi mà họ có thể tham khảo để đạt được câu trả lời chính xác hơn.

        *Câu hỏi từ người dùng*: {query}

        Hãy trả lời một cách chi tiết, rõ ràng và chính xác bằng Tiếng Việt. Đảm bảo rằng câu trả lời của bạn không chỉ đầy đủ mà còn có tính linh hoạt, giúp người dùng không chỉ trả lời câu hỏi mà còn khám phá thêm thông tin có giá trị từ bộ dữ liệu.
        """
    )
    return generate_openai_response(system_prompt)


tableau_embed_code = """
<div style='display: flex; justify-content: center; align-items: center; width: 100%; height: 100vh;'>
    <div class='tableauPlaceholder' id='viz1736519773696' style='position: relative; width: 100%; height: 100%; max-width: 100%; max-height: 100vh;'>
    <noscript>
        <a href='#'>
            <img alt='Nhà thuốc' src='https://public.tableau.com/static/images/Da/Dashboard_Chatbot/Nhthuc/1_rss.png' style='border: none' />
        </a>
    </noscript>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='Dashboard_Chatbot/Nhthuc' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https://public.tableau.com/static/images/Da/Dashboard_Chatbot/Nhthuc/1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
    </object>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1736519773696');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if (divElement.offsetWidth > 800) {
        vizElement.style.width = '100%';
        vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
    } else if (divElement.offsetWidth > 500) {
        vizElement.style.width = '100%';
        vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
    } else {
        vizElement.style.width = '100%';
        vizElement.style.height = '2677px';
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
</div>
"""

# Use a container to set the maximum width and height
st.markdown("""
    <style>
        .stApp {
            max-width: 100%;
            padding: 0;
        }
        iframe {
            width: 100%;
            height: 100vh;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# Display the centered and responsive Tableau embed
st.components.v1.html(tableau_embed_code, height=1000, scrolling=False)

# HTML for toggle button and chat container
st.markdown(
    """
    <div class="chat-container">
        <h2>Trợ lý AI báo cáo dữ liệu</h2>
    """,
    unsafe_allow_html=True
)

# Initialize chat session variables if not already set
if "chat_active" not in st.session_state:
    st.session_state.chat_active = False

# Display chat messages (no history saving)
with st.container():
    # Chat input
    user_input = st.chat_input("Hãy đặt câu hỏi về bộ dữ liệu:")

    if user_input:
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate AI response
        response = process_user_query(user_input)

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)


# Close chat container
st.markdown("</div>", unsafe_allow_html=True)
