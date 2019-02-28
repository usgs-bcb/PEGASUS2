# OBIS and the EOVs for Biodiversity
This repo contains some work on examining how the Ocean Biogeographic Information System (OBIS) can play a role in the process toward implementing the [Essential Ocean Variables for Biodiversity](http://www.goosocean.org/index.php?option=com_content&view=article&id=14&Itemid=114). OBIS is the world's largest aggregation of biological observation and measurements and may be able to serve a central role in helping to operationalize some of the EOV subvariables and derivative reporting products. It has the following types of information characteristics that should contribute:

* Taxonomic information aligned with the World Register of Marine Species (WoRMS). Observation records for individual organisms or records of groups of species (77% of OBIS records are at the species level) are identified with a WoRMS identifier. The continuous integration process in OBIS infuses fresh WoRMS taxonomy into the data, enabling rich taxonomic search and analysis. This capability may support EOV subvariables on species diversity, in particular.
* Records are identified temporally and spatially (full x,y and z) in many cases. This information comes along with specified uncertainty per record or dataset to help hone in on data appropriate for particular analyses such as distribution modeling.
* OBIS now supports and is beginning to integrate data that are organized on sampling events, rather than simply a species occurrence, and include observations and measurements beyond a single species. This accommodates data that estimate species abundance or coverage along with additional in situ measurements of environmental conditions at the point of observation.
* The continuous integration process in OBIS incorporates an area of interest indexing routine that adds identifiers for areas such as Large Marine Ecosystems, Ecologically and Biologically Significant Areas, and a reasonable interpretation of EEZ areas for countries. This feature can support building subvariables and derivatives within policymaking contexts.

The notebooks contain notes about a developing process to identify taxonomic groups associated with the EOVs and various ways of querying and working with OBIS data. This is meant as a living resource that will be built upon by others following a PEGASuS workshop the week of March 4.