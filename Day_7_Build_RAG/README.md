# Day 7 — Build RAG

Build a system that finds relevant information before asking an AI model to answer, then improve the evidence that reaches the model.

**RAG means Retrieval Augmented Generation:** retrieve useful passages from your data, include those passages with the question, and generate an answer using that context.

These are guided **learner notebooks with TODOs**, not completed applications. Work through the cells in order, complete each exercise, and inspect its output before continuing.

## The two assignments

| Notebook | What you build | What you learn |
| --- | --- | --- |
| [Assignment 1 — Multimodal RAG](assignment_1_multimodal_rag.ipynb) | A pipeline that loads files, stores text embeddings in LanceDB, retrieves passages, and answers questions through OpenRouter, with a Gradio interface. | Loading, chunking, embeddings, vector storage, retrieval, and the difference between retrieved evidence and a generated answer. |
| [Assignment 2 — Advanced RAG](assignment_2_advanced_rag.ipynb) | A pipeline that cleans up retrieved passages from a sample company handbook and returns validated structured answers. | Similarity filtering, metadata filtering, deduplication, reranking, and Pydantic validation. |

Start with Assignment 1 for the foundations. Assignment 2 builds on those concepts but includes its own data and index setup; it does not require files or a saved index produced by Assignment 1.

## Before you begin

- Use **Google Colab**. Both notebooks read the API key through Colab Secrets; Assignment 1 also mounts Google Drive.
- Create an OpenRouter API key, add it to Colab's Secrets panel as **`OPENROUTER_API_KEY`**, and enable notebook access. Keep the key out of notebook cells and shared screenshots.
- Check credits and access to the configured model with your host. Both notebooks currently specify `openai/gpt-5-mini`; update their configuration if the host selects a different available model. Assignment 2's structured-output exercises also require JSON-mode support.
- Allow time for package installation and the first download of the local embedding and reranking models. Runtime depends on the environment and data size.

## Open the notebooks in Colab

1. Open [Google Colab](https://colab.research.google.com/).
2. Choose **File → Open notebook → GitHub** and paste the C11 repository URL: `https://github.com/eng-accelerator/ai-accelerator-C11`.
3. Select a notebook under `Day_7_Build_RAG` and save a copy to your Drive so you can keep your edits. Alternatively, download the notebook from GitHub and upload it to Colab.
4. Connect the runtime, configure the secret, and follow the setup cells.
5. Run cells from top to bottom. Replace the TODO placeholders and uncomment the required return statements before testing each function. Running all cells immediately will fail because the exercises are unfinished.

## Assignment 1 — From files to answers

### Workflow

1. Mount Drive and install the dependencies.
2. Set the data and storage paths in `CONFIG`.
3. Configure the local embedding model and text chunking.
4. Inspect the dataset, then load its files as documents.
5. Create the LanceDB vector store and connect it through `StorageContext`.
6. Build and persist the vector index.
7. Retrieve relevant chunks and inspect their scores, file names, and text.
8. Combine the retrieved text with the question and call OpenRouter.
9. Launch the supplied Gradio app to display an answer alongside retrieved sources.

### Update the paths first

The notebook contains classroom-specific paths that **will not automatically exist in your Drive**:

| Setting | Path currently in the notebook | What to change |
| --- | --- | --- |
| Dependency installation | `/content/drive/MyDrive/outskill_c11/requirements.txt` | Point to your copy of the class requirements file. |
| `CONFIG["data_path"]` | `/content/drive/MyDrive/outskill_c4/data` | Point to the folder containing your input documents. |
| Vector and index storage | `/content/storage/...` | These are Colab runtime paths; copy the stored data to Drive if you need it after the runtime ends. |

The [Day 6 requirements file](../Day_6_Atlas/session_2/requirements.txt) and [Day 6 sample data](../Day_6_Atlas/session_2/data) are available in this repository. Download or copy them into your Drive and update the notebook paths accordingly. Opening the notebook from GitHub does not download these supporting files into your Drive. The notebook separately installs Gradio, FFmpeg, and Whisper.

The exercise loads mixed file types, but its retrieval and final answer use **extracted text** and text embeddings. Image and audio usefulness depends on the reader and any OCR or transcription available; do not assume that loading a file automatically makes every visual or audio detail searchable. Start with readable text documents if a format-specific reader causes problems.

### Expected output

- A dataset summary and a nonzero number of loaded documents.
- A vector index and retrieved passages with scores and source metadata.
- An answer to a question supported by your documents.
- A Gradio page titled **Multimodal RAG Question Answering**, with **Question**, **Answer**, and **Retrieved sources** fields.

Try a question you know the data can answer, such as the supplied travel or cooking examples when using the Day 6 dataset. Answer wording varies. Retrieved sources help you inspect the evidence; their presence alone does not prove that the generated answer is correct.

The Gradio cell uses `share=True`, creating a temporary public link. Use workshop data and avoid private information in the shared app.

## Assignment 2 — Improve retrieval and structure the answer

This notebook contains a fictional **Brightwave company handbook** with 16 sections. Some passages are outdated, duplicated, unrelated, or appear relevant without actually answering the question. No Drive dataset or LanceDB setup is needed for this assignment; its vector index is built in memory.

### Workflow

1. Install the packages and configure the OpenRouter secret.
2. Build an index over the included handbook and inspect the top 10 results.
3. Apply a **similarity cutoff** to remove weak matches.
4. Apply a **metadata filter** to keep the selected policy year.
5. Remove near-duplicate text using word overlap.
6. Use a **cross-encoder reranker** to reorder the remaining evidence and retain the best three chunks.
7. Compare generated answers with and without post-processing.
8. Define and validate structured answers with **Pydantic**.
9. Extract typed policy fields and compare them using Python.

### Expected output

- Lists of retrieved chunks showing scores, policy years, and source file names.
- For the main leave-policy question, the notebook's reference progression is **10 → 6 → 5 → 4 → 3** chunks. Exact scores, ordering, and counts can vary with model or library changes; inspect the evidence rather than treating those counts as a universal rule.
- An answer grounded in the sample 2025 policy: **12 casual leave days**, rather than the outdated 2023 value of 8.
- A structured answer with `answer`, `sources`, `answer_found`, and `confidence` fields.
- Typed leave-policy data and a Python comparison showing a four-day increase in casual leave and 22 total leave days in the sample 2025 policy.
- Validation examples that accept a correctly shaped reply and reject missing fields or invalid values such as the word `"twelve"` in a numeric field.

The free-text generation function skips the LLM call when no chunks survive filtering. The later structured-answer exercise still calls the LLM with an explicit empty-context message. These are different behaviors to observe.

Pydantic checks the answer's structure and field types; it does **not** verify whether an answer is factually correct. Likewise, the model's `confidence` label is not a calibrated probability. Check the selected sources as well as the output format.

## When you get stuck

- **Missing key:** confirm the secret name and enable notebook access in Colab.
- **Folder or requirements file not found:** correct the Drive paths before proceeding.
- **`None`, an undefined variable, or an empty result after an exercise:** check whether its TODOs and return statements are complete, then rerun that cell and the dependent cells below it.
- **Sources appear but the answer is empty:** check the generation function, whether the retrieved chunks contain text, and the model response. Retrieval and generation are separate steps.
- **No chunks survive filtering:** inspect scores and metadata. A threshold suitable for one model or dataset may be unsuitable for another.
- **API errors:** check the key, credits, model availability, and JSON-mode support for structured output.

## What you should understand by the end

You should be able to explain how documents become searchable vectors, why retrieving a passage differs from generating an answer, how outdated or repeated evidence affects answers, and why an application may need validated structured data instead of free text.

Complete the experiments and reflection questions at the end of each notebook to connect these ideas to your own use case.
