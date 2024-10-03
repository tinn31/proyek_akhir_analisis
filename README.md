# Air Quality Dashboard

## Instructions to Set Up the Air Quality Dashboard

1. **Download the Dashboard Project:**
   - Click on the [link to your GitHub repository](https://github.com/tinn31/proyek_akhir_analisis.git) to access the project.
   - On the repository page, click the green **Code** button, and then select **Download ZIP**.
   - Alternatively, you can clone the repository using Git:
     ```bash
     git clone https://github.com/tinn31/proyek_akhir_analisis.git
     ```

2. **Extract the Downloaded File:**
   - If you downloaded the ZIP file, locate the file in your Downloads folder or the location you saved it.
   - Right-click the ZIP file and select **Extract All**. Follow the prompts to extract the contents to a desired location on your computer.
   - extract file combined_data.zip

3. **Open Command Prompt (cmd):**
   - Press `Win + R`, type `cmd`, and hit `Enter` to open the Command Prompt.

4. **Navigate to the Project Directory:**
   - Use the `cd` command to change to the directory where you extracted the project. For example:
     ```bash
     cd E:\sertif\app
     ```

5. **Set Up the Virtual Environment:**
   - Create a virtual environment by running:
     ```bash
     python -m venv env
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\env\Scripts\activate
       ```
     - On Mac/Linux:
       ```bash
       source env/bin/activate
       ```

6. **Install Required Packages:**
   - Ensure your virtual environment is activated, then install the required packages using:
     ```bash
     pip install -r requirements.txt
     ```

7. **Run the Streamlit Application:**
   - After the installation is complete, start the application with:
     ```bash
     streamlit run app.py
     ```

8. **Open the Dashboard in Your Browser:**
   - A new tab should open in your default web browser, displaying the Air Quality Dashboard. If it doesn't open automatically, you can manually navigate to `http://localhost:8501`.

## Additional Notes
- Ensure you have Python 3.x installed on your system before proceeding with the installation steps.
- If you encounter any issues, please refer to the documentation or the issues section of the GitHub repository for troubleshooting.
