import json
import gradio as gr
from schema_miner.utils import read_json_file

with gr.Blocks() as schema_miner_stage1:
    gr.Markdown(
        """
        # Schema Miner - Initial Schema Mining 
        **Welcome to Schema Miner** — a Human-in-the-Loop framework for Scientific Schema Mining using Large Language Models (LLMs). This tool is designed to assist you in extracting structured schema representations for scientific processes by leveraging scientific literature and continuous human feedback.
        This interactive demo will guide you step-by-step, starting from unstructured textual information and culminating in a well-defined, structured schema. Each tab above corresponds to a distinct stage in the Schema Miner workflow, progressively refining and enriching the extracted schema with domain knowledge.
        In this first stage, the LLM generates an initial JSON schema that captures essential properties, data types, and associated constraints relevant to the target scientific domain. This foundational schema acts as the basis for subsequent stages, where it is iteratively improved using expert input and ontological alignment.
        To get started, simply enter your OpenAI API key, provide a brief description of the target process, and upload a process specification document. Once submitted, the system will automatically generate an initial schema representation, marking the beginning of your schema discovery journey.
        """
    )

    with gr.Group():
        api_key = gr.Textbox(
            label="OpenAI API Key",
            info="Please input your OpenAI API Key here. Please note that the key will only be used for this demo and will not be uploaded or used anywhere else."
        )
        api_key_btn = gr.Button(value="Submit API Key")
        # api_key_btn.click(fn=set_openai_api_key, inputs=api_key, outputs=api_key)
    
    with gr.Row():
        with gr.Group():
            with gr.Column():
                stage1_chatbot = gr.Chatbot([
                    {
                        'role': 'assistant', 
                        'content': 'Hello! I am Schema Miner, your assistant for extracting an initial schema from a scientific process specification. To begin, could you please provide the name of the scientific process you are working with?'
                    }],
                    type = 'messages')
                stage1_chat_input = gr.Textbox(
                    placeholder="Please type your message here and press Enter to interact with the chatbot!",
                    show_label=False
                )
        with gr.Group():
            with gr.Column():
                process_specification_doc = gr.File(
                    file_count = 'single',
                    file_types = ['.pdf'],
                    label = 'Upload Process Specification Document',
                    height = 420
                )
                generate_schema_but = gr.Button('Generate Schema')
    
    gr.Markdown(
        """
        # Extracted JSON Schema
        Below is the initial schema representation automatically generated from your **Process Specification Document**. Please review the extracted schema carefully and proceed to the next stage for further refinement and validation with domain-specific knowledge.
        """
    )
    
    with gr.Row():
        generated_schema_stage1 = gr.TextArea(
            placeholder = json.dumps(read_json_file('schema_miner/json_template.json'), indent=4),
            interactive=False,
            show_label = False
        )

with gr.Blocks() as schema_miner_stage2:
    gr.Markdown(
        """
        # Schema-Miner - Preliminary Schema Refinement 
        You have now entered the second stage of the Schema Miner workflow. In this phase, the initial schema is systematically improved by analyzing a curated collection of scientific literature and incorporating feedback from domain experts. This human-in-the-loop approach ensures the schema evolves to become both domain-specific and generalizable, capturing structural and semantic consistency across varied research workflows. At each iteration, experts review the schema to identify gaps, correct inaccuracies, and enrich it with deeper contextual understanding. Please follow the instructions below to begin refining your initial schema."""
    )

    with gr.Group():
        api_key = gr.Textbox(
            label="OpenAI API Key",
            info="Please input your OpenAI API Key here. Please note that the key will only be used for this demo and will not be uploaded or used anywhere else."
        )
        api_key_btn = gr.Button(value="Submit API Key")
        # api_key_btn.click(fn=set_openai_api_key, inputs=api_key, outputs=api_key)

    with gr.Row():
        with gr.Group():
            with gr.Column():
                stage2_chatbot = gr.Chatbot([
                    {
                        'role': 'assistant', 
                        'content': 'Hello! I am Schema Miner, your assistant for refining the initial schema. To begin, please upload a scientific paper that will be used to enhance and enrich your existing schema representation.'
                    }],
                    type = 'messages')
                stage2_chat_input = gr.Textbox(
                    placeholder="Please type your message here and press Enter to interact with the chatbot!",
                    show_label=False
                )
        with gr.Group():
            with gr.Column():
                scientific_paper = gr.File(
                    file_count = 'single',
                    file_types = ['.pdf'],
                    label = 'Upload Scientific Paper',
                    height = 420
                )
                upload_paper_but = gr.Button('Upload')
    
    gr.Markdown(
        """
        # Extracted JSON Schema
        Below is the refined schema representation, enhanced using the scientific literature you provided and iterative human feedback. Please review the updated schema carefully, and when ready, proceed to the next stage for further refinement and validation.
        """
    )
    
    with gr.Row():
        generated_schema_stage2 = gr.TextArea(
            placeholder = json.dumps(read_json_file('schema_miner/json_template.json'), indent=4),
            interactive=False,
            show_label = False,
            lines = 13
        )

with gr.Blocks() as schema_miner_stage3:
    gr.Markdown(
        """
        # Schema Miner - Finalize Schema Refinement 
        You have now reached the third stage of the Schema Miner workflow. In this phase, the schema is further refined and validated using a larger, uncurated corpus of scientific papers, enhancing its structural completeness, semantic richness, and generalizability. The LLM analyzes this broader dataset to incorporate new properties, address omissions, and ensure appropriate data types and constraints, all while avoiding redundancy and irrelevant additions. Throughout this process, domain-expert feedback remains essential, guiding iterative updates to maintain accuracy, semantic consistency, and alignment with real-world scientific discourse. Please follow the instructions below to begin refining your schema.
        """
    )

    with gr.Group():
        api_key = gr.Textbox(
            label="OpenAI API Key",
            info="Please input your OpenAI API Key here. Please note that the key will only be used for this demo and will not be uploaded or used anywhere else."
        )
        api_key_btn = gr.Button(value="Submit API Key")
        # api_key_btn.click(fn=set_openai_api_key, inputs=api_key, outputs=api_key)

    with gr.Row():
        with gr.Group():
            with gr.Column():
                stage3_chatbot = gr.Chatbot([
                    {
                        'role': 'assistant', 
                        'content': 'Hello! I am Schema Miner, your assistant for refining the schema. To begin, please upload a scientific paper that will be used to enhance and enrich your existing schema representation.'
                    }],
                    type = 'messages')
                stage2_chat_input = gr.Textbox(
                    placeholder="Please type your message here and press Enter to interact with the chatbot!",
                    show_label=False
                )
        with gr.Group():
            with gr.Column():
                scientific_paper = gr.File(
                    file_count = 'single',
                    file_types = ['.pdf'],
                    label = 'Upload Scientific Paper',
                    height = 420
                )
                upload_paper_but = gr.Button('Upload')
    
    gr.Markdown(
        """
        # Extracted JSON Schema
        Below is the refined schema representation, enhanced using the scientific literature you provided and iterative human feedback. Please review the updated schema carefully, and when ready, proceed to the next stage for ontology grounding.
        """
    )
    
    with gr.Row():
        generated_schema_stage2 = gr.TextArea(
            placeholder = json.dumps(read_json_file('schema_miner/json_template.json'), indent=4),
            interactive=False,
            show_label = False,
            lines = 13
        )

demo = gr.TabbedInterface(
    [schema_miner_stage1, schema_miner_stage2, schema_miner_stage3],
    ['Stage-1: Initial Schema Mining', 'Stage-2: Preliminary Schema Refinement', 'Stage-3: Finalize Schema Refinement']
)


if __name__ == "__main__":
    demo.launch()