"""cve_migration

Revision ID: b23c87b98385
Revises: e8760725610a
Create Date: 2020-03-30 14:33:17.731614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b23c87b98385"
down_revision = "e8760725610a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cve_packages",
        sa.Column("cve_id", sa.Integer(), nullable=True),
        sa.Column("package_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.Integer(), nullable=True),
        sa.Column(
            "type",
            sa.Enum("package", "product", "snap", name="packagetype"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(["cve_id"], ["cve.id"],),
        sa.ForeignKeyConstraint(["name"], ["release.id"],),
        sa.ForeignKeyConstraint(["package_id"], ["package.id"],),
    )
    op.add_column(
        "cve",
        sa.Column(
            "status",
            sa.Enum("rejected", "active", "not_for_us", name="cvestatus"),
            nullable=True,
        ),
    )
    op.drop_constraint(
        "package_release_status_name_fkey",
        "package_release_status",
        type_="foreignkey",
    )
    op.drop_column("package_release_status", "type")
    op.drop_column("package_release_status", "name")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "package_release_status",
        sa.Column("name", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "package_release_status",
        sa.Column(
            "type",
            sa.ENUM("package", "product", "snap", name="packagetype"),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.create_foreign_key(
        "package_release_status_name_fkey",
        "package_release_status",
        "release",
        ["name"],
        ["id"],
    )
    op.drop_column("cve", "status")
    op.drop_table("cve_packages")
    # ### end Alembic commands ###