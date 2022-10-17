import os
import datetime as dt

class fileName():
    def __init__(self,project_name: str=None, components: list=None, date: str=None, suffix: str=None, output_dir: str=None):

        self.name=''
        if project_name is None:
            pass
        else:
            self.name += self.check_for_separator(project_name,-1,'_')

        if components is None:
            pass
        else:
            for comp in components:
                self.name+=self.check_for_separator(comp,-1,'_')

        self.date=date
        if self.date is None:
            self.date=dt.date.today().strftime('%Y-%m-%d')

        if suffix is None:
            pass
        else:
            self.suffix=self.check_for_separator(suffix,0,'.')

        if output_dir is None:
            output_dir=''
        self.out_dir=output_dir

    def check_for_separator(self,string: str, pos: str='s', separator='_') -> str:
        """ Check if character at pos of string is separator, and if not, inserts it there.
            pos = 's' checks first caracter of string, pos = 'e' checks last
            NOTE: This doesn't have to be a class method in this form...
        """
        out = string
        if pos in ['s',0]:
            pos = 0
        elif pos in ['e',-1]:
            pos=-1
        else:
            raise Exception("pos keyword has to be either of 's' (start) or 'e'\
                            (end). ")
        if out[pos]==separator:
            pass
        else:
            if pos == 0:
                out = separator+out
            else:
                out = out+separator
        return out

    def append_components(self,append: list):
        """
        Return name with additional components added (separated by '_').
        """
        out = self.name
        if append is not None:
            for comp in append:
                out += self.check_for_separator(comp,-1,'_')
        return out

    def get_name(self,append: list=None,suffix: str=None):
        """
        Build and return name, prepending with out_dir,
        appending components to name, and adding the
        date and suffix.
        """
        if suffix is None and self.suffix is None:
            raise Exception('No suffix specifed in contructor nor at method call.')
        elif suffix is None:
            suffix=self.suffix
        elif isinstance(suffix,str):
            suffix = self.check_for_separator(suffix,0,'.')


        return os.path.join(self.out_dir,self.append_components(append)+self.date+suffix)

if __name__ == '__main__':
    project = 'project'
    components = ['test','alpha_']
    suffix = 'txt'
    append = ['v2','beta_']
    name = fileName(project_name=project,components=components,suffix=suffix)
    print(name.get_name(append=append,suffix='pdf'))
