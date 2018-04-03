from distutils.core import setup

#ficheiros= ["Cousas/*"]
setup(name = "MascotasProxecto",
      version="0.01",
      description="Aplicacion de exemplo de distribucion",
      long_description="""Descripcion en mais dunha liña
      extensa da aplicacion""",
      author="Christian",
      author_email="csantamariacameselle@danielcastelao.org",
      url="www.urldoproxecto.es",
      keywords="Proba, distribuicion, exemplo",
      platforms="linux, mac",
      packages=['Paquete'],
      #packages= find_packages(),
      #package_data={'Paquete': ficheiros},
      scripts=["Lanzador"],
      #py_modulos= ["moduloProbraModulo"]
      #install_requires= ["paquete_requerido >= 1.0 < 2.2"]

      )
#setup_requires
#test_requires

