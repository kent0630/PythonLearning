EPYDOC=epydoc  
DSTDOC=docstrings  
      
doc: clean-doc
	$(EPYDOC) --html --graph=all -v -o $(DSTDOC) l_doctest.py
      
clean-doc:
	rm -rf $(DSTDOC)
      
clean: clean-doc
	find . \( -name '*~' -or \  
		 -name '*.pyc' -or \  
		 -name '*.pyo' \) \  
		 -print -exec rm {} \;  
