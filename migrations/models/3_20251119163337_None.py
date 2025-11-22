from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(50) NOT NULL UNIQUE,
    `password` VARCHAR(128) NOT NULL,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4 COMMENT='用户模型';
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlm1v2jAQx78KyqtO6ipIedLeUcZUpgETpdvUUkUmNiEisdPYKUUV330+JyFPhNJpG6"
    "3UNyi5+59z9zusuyfNZZg4/OyaE380HmifKk8aRS6RD3nXaUVDnpc4wCDQzFHaQIqUBc24"
    "8JEppHGOHE6kCRNu+rYnbEZBOg1aDb09DZr6eUv+Ir02DRqt9gyiMTNluE2t54QBte8DYg"
    "hmEbEgvpTf3kmzTTF5JDx+9ZbG3CYOzpRlYzhA2Q2x9pStT8UXJYQcZobJnMClidhbiwWj"
    "W7VNBVgtQomPBIHjhR9AqTRwnAhJXH2YaSIJU0zFYDJHgQPAILrAKzamyEQmk1FgLbPhqk"
    "ALvvJRr9Vb9fZ5s96WEpXJ1tLahOUltYeBisBwom2UHwkUKhTGhBu0WD0X6HUXyN+NLx2T"
    "gyhTz0OMkR2VooseDYdQSyzka6O6B9mPzrh72RmfNKofoBIm//bhZRhGHl25gGpC0UOcr5"
    "i/4z9YTjEd83coxoYEY3JZ/wXHmt4+AKRUlZJUvixK0ydQsoFEEeZn6RG2S3YDzUbmkOIo"
    "9Cx+eKWAZQ14RJ11dAf28J30B72rSWfwHSpxOb93FKLOpAceXVnXOetJM9eK7SGVn/3JZQ"
    "VeKzejYU8RZFxYvvpiopvcaJATCgQzKFsZCKeua2yNwWQaG3j4DxubjXxv7FEbq5KHMTxf"
    "pgYKGGbIXK6Qj42Ch+msTFt0ubqbtyCKLNUVYAtZRktMh/i2udi13kSevdsNSjTPrTflbX"
    "5fWf77yvIgl1JI6QWzNhXyNket3mgcMGqlqnTUKl921MLVeAHESP42Adaqhyx9UlW+q1QL"
    "a5/8oiB0xzz7ejUaliwpSUgO5DWVBd5i2xSnFcfm4u51Yt1DEarOzKwY3smg8yvPtfttdJ"
    "EfRnDAhWR81PGy+Q3kp9nJ"
)
