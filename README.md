# Simple-TrainBooking-Platform-Using-Flask
Simple Train Booking Web App using Flask: A basic Python Flask application simulating a train seat booking system. View available seats, book by seat type (Window/Middle), and cancel seats by position.
## Setup and Installation

1.  **Clone the repository (or create the files manually):**
    ```bash
    # If cloning from a repo
    git clone <your_repo_url>
    cd <your_repo_directory>

    # If creating files manually, ensure the directory structure above is followed.
    ```

2.  **Ensure you have Python installed:**
    If not, download it from [python.org](https://www.python.org/).

3.  **Install Flask:**
    It's recommended to use a virtual environment.
    ```bash
    # Create a virtual environment (optional but recommended)
    python -m venv venv
    # Activate the virtual environment
    # On Windows:
    # .\venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate

    # Install Flask
    pip install Flask
    ```

4.  **Place the provided files:**
    *   `app.py` in the root directory.
    *   `train.py` in the root directory.
    *   Create a `static` folder and place `style.css` inside it.
    *   Create a `templates` folder and place `index.html` inside it.

## Running the Application

1.  **Make sure your virtual environment is activated** (if you used one).
2.  **Run the Flask application:**
    ```bash
    python app.py
    ```
3.  **Open your web browser** and navigate to the address shown in the console (usually `http://127.0.0.1:5000/`).

## Usage

Once the application is running and you visit the URL:

*   **Available Seat Count:** Click the "Click Here" button next to "Awailable seate number are:". The page will update to show the count.
*   **Available Seat Positions:** Click the "Click Here" button next to "Awailable seate position are:". The page will update to show the current 2D grid of seats.
*   **Book Seat:**
    *   Select a seat type ("Window" or "Middle") from the dropdown.
    *   Click the "BookSeat" button.
    *   A message indicating the booked seat's position or "No Seats Available" will appear.
*   **Cancel Seat:**
    *   Select the Row index and Column index of the seat you wish to cancel from the respective dropdowns.
    *   Click the "CancleSeat" button.
    *   A confirmation message or an error ("Entered Wrong SeatID") will appear.

Each action triggers a page refresh to display the result.

## Potential Improvements

*   Implement persistent storage (e.g., using SQLite or another database) so seat data isn't lost on restart.
*   Create a more interactive UI (e.g., click on a seat in the grid to book/cancel, use JavaScript/AJAX to update parts of the page without full refresh).
*   Allow users to select a *specific* seat of a type to book, rather than just booking the first available.
*   Add more robust error handling and input validation (e.g., prevent cancelling an already available seat by selecting its old type).
*   Improve the visual representation of the seat map.
*   Add tests for the `Train` class logic.
