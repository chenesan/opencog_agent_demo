#!/bin/python

"""
This agent will randomly generate action(call function in schema).
To test it just define 'schema1', 'schema2' function in the opencog guile shell,
and load this py file.
"""


from opencog.atomspace import AtomSpace,types
from opencog.scheme_wrapper import scheme_eval

import opencog.cogserver
import random

class RandomActionGeneratorAgent(opencog.cogserver.MindAgent):

    def __init__(self):

        self.init=False;
        
    def run(self,atomspace):

        #Because I don't know how to add atom in cogserver in  __init__(),
        #so I add setlink in run().

        if self.init==False:

            self.execset=atomspace.add_link(types.SetLink,[
                atomspace.add_link(types.ExecutionOutputLink,[
                    atomspace.add_node(types.GroundedSchemaNode,'scm: schema1'),
                    atomspace.add_link(types.ListLink,[
                        atomspace.add_node(types.ConceptNode,"GoodJob")])]),
                atomspace.add_link(types.ExecutionOutputLink,[
                    atomspace.add_node(types.GroundedSchemaNode,'scm: schema2'),
                    atomspace.add_link(types.ListLink,[
                        atomspace.add_node(types.ConceptNode,"Hello")])])])

            self.init==True

        exechandle=self.execset.out[random.randint(0,1)].handle_uuid()
        scheme_eval(atomspace,'(cog-execute! (cog-atom %d))'%(exechandle))
