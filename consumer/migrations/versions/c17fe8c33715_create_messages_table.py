"""create messages table

Revision ID: c17fe8c33715
Revises:
Create Date: 2021-09-28 19:39:28.861217

"""
import uuid

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "c17fe8c33715"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "messages",
        sa.Column(
            "id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
        ),
        sa.Column("text", sa.String(1000)),
    )


def downgrade():
    sa.drop_table("messages")
