# -*- coding: utf-8 -*-
from libcomxml.core import XmlModel, XmlField


class Heading(XmlModel):
    _sort_order = ('heading', 'dispatchingcode',
                   'dispatchingcompany', 'destinycompany',
                   'communicationsdate', 'communicationshour', 'processcode',
                   'messagetype')

    def __init__(self):
        self.heading = XmlField('heading')
        self.dispatchingcode = XmlField('dispatchingcode')
        self.dispatchingcompany = XmlField('dispatchingcompany')
        self.destinycompany = XmlField('destinycompany')
        self.communicationsdate = XmlField('communicationsdate')
        self.communicationshour = XmlField('communicationshour')
        self.processcode = XmlField('processcode')
        self.messagetype = XmlField('messagetype')
        super(Heading, self).__init__('heading', 'heading')

