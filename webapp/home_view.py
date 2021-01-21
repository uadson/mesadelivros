from django.http import HttpResponse


def home(request):
	return HttpResponse(
		'''
			<hr>
			<h3>Biblioteca Digital</h3>
			<hr>
			<h4>Em Construção<h4>
			<a href="index/">Clique Aqui</a>
			<hr>
		'''
		)