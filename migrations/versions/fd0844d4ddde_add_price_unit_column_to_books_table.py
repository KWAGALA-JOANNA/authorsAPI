"""Add price_unit column to books table

Revision ID: fd0844d4ddde
Revises: d2861542b749
Create Date: 2024-03-16 18:40:37.200216

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fd0844d4ddde'
down_revision = 'd2861542b749'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price_unit', sa.String(length=10), nullable=False))
        batch_op.add_column(sa.Column('publication_date', sa.Date(), nullable=False))
        batch_op.add_column(sa.Column('isbn', sa.String(length=30), nullable=True))
        batch_op.add_column(sa.Column('genre', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('image', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('company_id', sa.Integer(), nullable=True))
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('description',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=255),
               nullable=False)
        batch_op.alter_column('price',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
        batch_op.create_unique_constraint(None, ['isbn'])
        batch_op.create_foreign_key(None, 'companies', ['company_id'], ['id'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.Text(),
               existing_nullable=False)
        batch_op.alter_column('biography',
               existing_type=mysql.VARCHAR(length=1000),
               type_=sa.Text(),
               existing_nullable=True)
        batch_op.alter_column('user_type',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.drop_index('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('password', ['password'], unique=True)
        batch_op.alter_column('user_type',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('biography',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=1000),
               existing_nullable=True)
        batch_op.alter_column('password',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('price',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.String(length=255),
               type_=mysql.TEXT(),
               nullable=True)
        batch_op.alter_column('title',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.drop_column('company_id')
        batch_op.drop_column('image')
        batch_op.drop_column('genre')
        batch_op.drop_column('isbn')
        batch_op.drop_column('publication_date')
        batch_op.drop_column('price_unit')

    # ### end Alembic commands ###
