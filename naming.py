import os
import datetime as dt

class fileName():
    def __init__(self,project_name: str=None, components: list=None, date: str=None, suffix: str=None, output_dir: str=None):

        self.name=''
        if project_name is None:
            pass
        else:
            if project_name[-1]=='_':
                pass
            else:
                project_name+='_'
            self.name+=project_name

        if components is None:
            pass
        else:
            for comp in components:
                if comp[-1]=='_':
                    pass
                else:
                    comp+='_'
                self.name+=comp

        if date is None:
            date=dt.date.today().strftime('%Y-%m-%d')
        self.name+=date

        if suffix is None:
            pass
        else:
            if suffix[0]=='.':
                pass
            else:
                suffix='.'+suffix
        self.suffix=suffix

        if output_dir is None:
            output_dir=''
        self.out_dir=output_dir


    def get_name(self,suffix: str=None):
        if suffix is None and self.suffix is None:
            raise Exception('No suffix speicifed in contructor nor at method call.')
        elif suffix is None:
            suffix=self.suffix

        return os.path.join(self.out_dir,self.name+suffix)
