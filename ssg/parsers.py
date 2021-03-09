import shutil
from typing import List
from pathlib import Path

class Parser:
    extensions: List[str] = [ ]

    
    def valid_extension(self,extension):
        return   extension in extensions
    
    
    def parse(self,path: Path,source: Path,dest:Path):
        raise not NotImplementedError
    
    def read(self,path):
        with open(path,"r") as file:
            return file.re()()
        
    def write(self,path,dest,content,ext=".html"):
        full_path=dest / path.with_suffix(ext).name
        with open (full_path,"r") as file :
            file.write(content)
            
    
        
    def copy(self,path,source,dest):
        shutil.copy2(path, dest/path.relative_to(source))
        
        
        class ResourceParser:
            
            
            extensions=['.jpg','.png','.gif','.css','.html']
            
            
            def parser(self,path,source,dest):
                copy(path,source,dest)