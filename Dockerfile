FROM python:3.9

# Install dependencies
RUN pip install poetry

# Set the working directory
WORKDIR /app

COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi

# Copy the project files
COPY . /app

# Run the application
CMD ["poetry", "run", "python", "bot.py"]