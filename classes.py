from sqlalchemy import ForeignKey, Column, Integer, Text, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Protein(Base):
    __tablename__ = "proteins"

    id = Column(String(4), primary_key=True)
    name = Column(Text)
    structure = Column(Text)
    chains = relationship("Chain", back_populates="protein")
    
    def __init__(self, id, name, structure):
        self.id = id
        self.name = name
        self.structure = structure

class Chain(Base):
    __tablename__ = "chains"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chain_id = Column(Text)
    sequence = Column(Text)
    esm = Column(Text)
    protein_id = Column(String(4), ForeignKey("proteins.id", ondelete='CASCADE'))
    protein = relationship("Protein", back_populates="chains")
    
    def __init__(self, protein_id, chain_id, sequence, esm=None):
        self.protein_id = protein_id
        self.chain_id = chain_id
        self.sequence = sequence
        self.esm = esm
