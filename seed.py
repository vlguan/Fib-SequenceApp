from sqlalchemy import create_engine, Table, MetaData, Column, Integer

# Set up the engine, which provides connectivity to the database.
engine = create_engine('sqlite:///server/instance/database.db')  # Use your database connection string.
metadata = MetaData()

# Define the table
fibonacci_numbers = Table(
    'fibonacci_numbers', metadata,
    Column('N', Integer, primary_key=True),
    Column('fib_num', Integer),
)

# Create the table
metadata.drop_all(engine)
metadata.create_all(engine)