inspired by David's talk https://www.youtube.com/watch?v=Obt-vMVdM8s&t, 
I attempt to evaluate the performace of using thread-like among languages.

# python thread
python perf.py 1000000 2

# python3.6 coroutine
python aperf.py 1000000 2

# go goroutine
go run perf.go 1000000 2

# java thead
javac perf.java -d . && java perf 1000000 2

# jython thread
java -jar jython-standalone-2.7.1.jar perf.py 1000000 2
(download jython 2.7.1 at http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7.1/jython-standalone-2.7.1.jar)