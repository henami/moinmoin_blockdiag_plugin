# -*- coding: utf-8 -*-
"""
    MoinMoin - diag Parser for blockdiag, nwdiag, seqdiag and actdiag.
    It also support rackdiag and packetdiag.

    @license: GNU GPL, see COPYING for details.
"""
__version__ = "1.0.0"

import re
#from pprint import pprint,pformat

class BlockDiagError(RuntimeError):
    pass

Dependencies = []

class Parser:
    module = None

    def __init__(self, raw, request, filename=None, format_args='', **kw):
        self.raw = raw
        self.request = request
        self.format_args = re.sub(r'[\,]',' ', format_args)

    def format(self, formatter, **kw):
        width, height = self._get_params(self.format_args)
        text = self.raw
        module_name = self.set_module(text)
        if self.module is None:
            self.request.write(formatter.preformatted(1))
            self.request.write('%s is invalid diag type or not implemented yet.' % module_name )
            self.request.write(formatter.preformatted(0))
            return
        tree = self.module.parser.parse_string(text)
        outfile = None
        diagram = self.module.builder.ScreenNodeBuilder.build(tree)
        DiagramDraw = self.module.drawer.DiagramDraw        
        draw = DiagramDraw('SVG', diagram, outfile, antialias=True, nodoctype=True)
        draw.draw()
        xy = draw.pagesize()
        svg = draw.save(None)
        if width is None:
            width = xy[0]
        if height is None:
            height = xy[1]
        #self.request.write(formatter.preformatted(1))
        self.request.write(self.svg_to_svg_fragment(svg, width, height))
        #self.request.write(formatter.preformatted(0))

    def svg_to_svg_fragment(self, svg, width, height):
        params = [(u"<\?xml.*\?>\n", u"",),
                  (u"<!DOCTYPE svg PUBLIC .*>\n", u"",), 
                  (u"<svg ", u"<svg width=%s height=%s preserveAspectRatio=\"meet\" " % (width, height)),]
        for pat, rep, in params:
            svg = re.sub(pat, rep, svg)
        return svg

    def _get_params(self, params):
        dparams = dict()
        if params is None:
            dparams['width'] = None
            dparams['height'] = None
        else:
            dparams = dict( t.split('=') for t in params.split() )
        width = dparams.get('width', None)
        height = dparams.get('height',None)
        return width, height

    def set_module(self, text):
        text = re.sub(r"^[\s\n]*", "", text) # omit empty line(s)
        first_line = (text.splitlines())[0];
        diag_type = re.sub(r"[\s\{].*", "", first_line);
        #self.request.write('<pre>')
        #self.request.write(pformat(diag_type))
        #self.request.write('</pre>')

        if diag_type == 'blockdiag':
            try:
                import blockdiag
                from blockdiag import builder
                from blockdiag import drawer
                from blockdiag import parser
                from blockdiag.parser import tokenize, parse
                self.module = blockdiag
            except ImportError:
                self.module = None
        elif diag_type == 'nwdiag':
            try:
                import nwdiag
                from nwdiag import builder
                from nwdiag import drawer
                from nwdiag import parser
                from nwdiag.parser import tokenize, parse
                self.module = nwdiag
            except ImportError:
                self.module = None
        elif diag_type == 'rackdiag':
            try:
                import rackdiag
                from rackdiag import builder
                from rackdiag import drawer
                from rackdiag import parser
                from rackdiag.parser import tokenize, parse
                self.module = rackdiag
            except ImportError:
                self.module = None
        elif diag_type == 'packetdiag':
            try:
                import packetdiag
                from packetdiag import builder
                from packetdiag import drawer
                from packetdiag import parser
                from packetdiag.parser import tokenize, parse
                self.module = packetdiag
            except ImportError:
                self.module = None
        elif diag_type == 'actdiag':
            try:
                import actdiag
                from actdiag import builder
                from actdiag import drawer
                from actdiag import parser
                from actdiag.parser import tokenize, parse
                self.module = actdiag
            except ImportError:
                self.module = None
        elif diag_type == 'seqdiag':
            try:
                import seqdiag
                from seqdiag import builder
                from seqdiag import drawer
                from seqdiag import parser
                from seqdiag.parser import tokenize, parse
                self.module = seqdiag
            except ImportError:
                self.module = None

        return diag_type
