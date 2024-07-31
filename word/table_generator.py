# https://misc.martinbisson.com/python/tabs/
import win32com
from datetime import datetime
class WordTabsGenerator:
    """The class that handles the generation of a Word document from tabs in
    .txt files."""
    
    # Word application object.
    app = None
    # Word document object.
    doc = None
    
    def Open(self, filename):
        """This function opens Word and creates the document."""
        
        # Initialize Word in a way that will initialize the constants as well.
        self.app = win32com.client.gencache.EnsureDispatch('Word.Application')
        #self.app = win32com.client.Dispatch('Word.Application')
        self.app.Visible = 1
        
        # Get a new document and save it.
        self.doc = self.app.Documents.Add()
        self.doc.SaveAs(filename)
        
        
    def PrepareDocument(self):
        """This function sets the properties that are commun to the whole
        document."""
        
        # Set the margins for the section section.
        MARGIN_SIZE = 50
        self.doc.PageSetup.LeftMargin   = MARGIN_SIZE
        self.doc.PageSetup.TopMargin    = MARGIN_SIZE
        self.doc.PageSetup.BottomMargin = MARGIN_SIZE
        self.doc.PageSetup.RightMargin  = MARGIN_SIZE

        # Prepare the document to remove spacing.
        for paragraph in self.doc.Paragraphs:
            paragraph.LineSpacingRule = win32com.client.constants.wdLineSpaceSingle
            paragraph.SpaceBefore     = 0
            paragraph.SpaceAfter      = 0
            
        # Prepare the document to set the font.
        self.SetStyle(self.doc.Content, -1)
        
        
    def GenerateCoverPage(self):
        """This function generates the cover page."""
        
        # Constants
        NB_ENTER_START   = 1
        NB_ENTER_BETWEEN = 13
        # Lines to add to the cover page.
        if True:
            import locale
            locale.setlocale(locale.LC_ALL,'french')
            today = datetime.date.today()
            day = today.day
            date_string = str(day)
            if (day == 1):
                date_string += 'er'
            date_string += ' '
            date_string += today.strftime('%B %Y')
        else:
            date_string = today.isoformat()
        lines = [
            ( ( 36 , False ) , 'Martin Bisson' ) ,
            ( ( 48 , True  ) , 'Mes Tablatures' ) ,
            ( ( 36 , False ) , 'Généré automatiquement' ) ,
            ( ( 36 , False ) , date_string )
            ];
            
        # Ranges to hold the font size.
        fonts = []
            
        coverpage = '\n' * NB_ENTER_START
        for line in lines:
            # Add the spacing.
            if line != lines[0]:
                coverpage += '\n' * NB_ENTER_BETWEEN
                
            # Add the string
            start = len(coverpage)
            coverpage += line[1]
            end = len(coverpage)
            fonts.append( ( line[0] , start , end ) )
            
        # Add the lines.
        range0 = self.doc.Range(0, 0)
        range0.InsertBefore(coverpage)
        range1 = self.doc.Range(range0.End, range0.End)
        range1.InsertBreak()
        
        
        # Set the fonts.
        for font in fonts:
            range = self.doc.Range(font[1], font[2])
            range.Font.Size = font[0][0]
            range.Font.Bold = font[0][1]
            
        # Center the paragraphs.
        for paragraph in range0.Paragraphs:
            paragraph.Alignment       = win32com.client.constants.wdAlignParagraphCenter
            
            
    def GenerateTableOfContents(self):
        """This function generates the table of content page."""
        
        # Insert title.
        range = self.AddTitle(self.GetRangeAtEnd(), 1, 'Table des matières')
        
        # Remember where to put the table.
        range_table = self.doc.Range(range.End, range.End)
        
        # Put the section break.
        range = self.doc.Range(range.End, range.End)
        range.InsertBreak(win32com.client.constants.wdSectionBreakNextPage)
        
        # Insert the table of content.
        self.doc.TablesOfContents.Add(range_table)
        
        
    def SetupSections(self):
        """This function sets up the different parameters for each section."""
        
        # Setup the page numbers.
        self.doc.Sections(1).PageSetup.DifferentFirstPageHeaderFooter = True
        self.doc.Sections(1).Headers(
            win32com.client.constants.wdHeaderFooterPrimary
            ).PageNumbers.ShowFirstPageNumber = False
        self.doc.Sections(1).Headers(
            win32com.client.constants.wdHeaderFooterPrimary
            ).PageNumbers.NumberStyle = win32com.client.constants.wdPageNumberStyleLowercaseRoman
        
        self.doc.Sections(2).Headers(
            win32com.client.constants.wdHeaderFooterPrimary
            ).PageNumbers.RestartNumberingAtSection = True
            
        self.doc.Sections(2).Headers(
            win32com.client.constants.wdHeaderFooterPrimary
            ).PageNumbers.StartingNumber = 1
            
            
    def GenerateTablatures(self, info, linebreaks):
        """This function generates the tabs pages."""
        
        for category in info:
            # First, an almost empty page just describing the category.
            range = self.AddTitle(self.GetRangeAtEnd(), 1, category[0])

            # Insert the text of the section.
            text_start = range.End;
            range.InsertAfter(
                '\tCette section contient les tablatures provenant des ' +
                'fichiers contenus dans le répertoire « ' + category[0] + ' ».'
                )
            text_end = range.End
            range = self.doc.Range(range.End, range.End)
            range.InsertBreak()

            # Set the size of the text.
            self.doc.Range(text_start, text_end).Font.Size = 12
            
            # Add the files
            for filename in category[1]:
                # Read the file.
                file = open(filename)
                lines = file.readlines()
                file.close()
                
                title = lines[0].strip()
                artist = lines[1].strip()
                # Get the first non empty line.
                i = 2;
                while i < len(lines) and len(lines[i].strip()) == 0:
                    i = i + 1
                lines = lines[i:]
                
                # Check for lines that are too long.
                MAX_NUMBER_OF_CHARS_PER_LINE = 85
                i = 0
                while i < len(lines):
                    if len(lines[i]) - 1 > MAX_NUMBER_OF_CHARS_PER_LINE:
                        print filename + ' : line ' + str(i) + ' is too long.'
                    i = i + 1
                
                # Add the title for that page.
                page_title = artist + ' - ' + title
                range = self.AddTitle(self.GetRangeAtEnd(), 2, page_title)
                
                # Gets the before which inserting a page break.
                try:
                    break_lines = linebreaks[page_title]
                except KeyError:
                    break_lines = []
                
                # Builds the sections separated by a page break.
                sections = [ '' ]
                i = 0
                while i < len(lines):
                    if break_lines.count(i) > 0:
                        sections.append('')
                    sections[-1] += lines[i]
                    i = i + 1
                    
                for section in sections:
                    # Insert the text.
                    range.InsertAfter(section)
                    range_section = self.doc.Range(range.Start, range.End)
                    range.Start = range.End
                    
                    # Insert the break.
                    range.InsertBreak()
                    range.Start = range.End
                    
                    # Set the font.
                    range_section.Font.Size = 10
                    
                    
    def Close(self):
        """This function closes the document and Word."""
        
        # Update the table of content.
        for table in self.doc.TablesOfContents:
            table.Update()
        
        # Close the document.
        #self.doc.Save()
        #self.doc.Close()
        #self.doc = None
        #
        ## Close Word.
        #self.app.Quit()
        #self.app = None
        
        
    def AddTitle(self, range, style, title):
        """This function adds a title to a page."""
        
        # Create the new range.
        range = self.doc.Range(range.End, range.End)
        range.InsertAfter(title)
        range_title = self.doc.Range(range.Start, range.End)
        
        # Add the enters.
        range.InsertAfter('\n' * 2)
        
        # Set the style.
        self.SetStyle(range_title, style)
        
        return self.doc.Range(range.End, range.End)
        
        
    def SetStyle(self, range, style):
        """This function sets the style on a given range."""
        
        # First set the style, if needed
        if (style == 1):
            range.Style = win32com.client.constants.wdStyleHeading1
        elif (style == 2):
            range.Style = win32com.client.constants.wdStyleHeading2
            
        # Then set the font.
        range.Font.Name = 'Courier New'
        
        
    def GetRangeAtEnd(self):
        """This function returns a Range object at the end of the document."""
        end = self.doc.Content.End - 1
        return self.doc.Range(end, end)
        
        
        
        
def GetTablatureFilesInfo(folder):
    """This function returns the tablature files ina a sorted way that can be
    used by the application to generate the Word document."""
    
    # Get all the subfolders in the given folder.
    folders = []
    for file in os.listdir(folder):
        if os.path.isdir(folder + '/' + file):
            folders.append(file)
    folders.sort()
    
    info = []
    for entry in folders:
        files = os.listdir(folder + '/' + entry)
        if len(files) != 0:
            # Append the folder names to the files.
            files_full = []
            for file in files:
                files_full.append(folder + '/' + entry + '/' + file)
            info.append( ( entry[3:] , files_full ) )
            
    return info




# To be able to use this file as a stand-alone and an importable module
if __name__ == '__main__':
    # Make sure a folder has been given.
    if len(sys.argv) != 2:
        raise Exception('Usage is "' + sys.argv[0] + ' tabs_folder/"')
    
    tabs_folder = sys.argv[1]
    
###    # Create the generator.
###    gen = WordTabsGenerator()
###    
###    # Open the Word file.
###    gen.Open(os.getcwd() + "/tabs.docx")
###    
###    gen.doc.Content.Text = ''
###    
###    # Generate the file.
###    gen.PrepareDocument()
###    gen.GenerateCoverPage()
###    gen.GenerateTableOfContents()
###    gen.SetupSections()
###    info = GetTablatureFilesInfo(tabs_folder)
###    gen.GenerateTablatures(info, page_breaks)
###    
###    # Close the Word file.
###    gen.Close()
    info = GetTablatureFilesInfo(tabs_folder)
    for category in info:
        for filename in category[1]:
            infile = open(filename)
            lines = infile.readlines()
            infile.close()
            
            outfile = open(filename, 'w')
            for line in lines:
                if line[-2:] == '\r\n':
                    line = line[:-2] + '\n'
                outfile.write(line)
            outfile.close()