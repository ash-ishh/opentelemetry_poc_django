from django.http import HttpResponse
from fibonacci.utils import fib_fast, fib_slow
from opentelemetry import trace


def calculate(request):
    n = request.GET.get('n', 1)
    if n.isnumeric():
        n = int(n)
    else:
        return HttpResponse(f'Calculation for {n} is not supported', status=415)
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("root"):
        with tracer.start_as_current_span("fib_slow") as slow_span:
            ans = fib_slow(n)
            slow_span.set_attribute("n", n)
            slow_span.set_attribute("nth_fibonacci", ans)
        with tracer.start_as_current_span("fib_fast") as fast_span:
            ans = fib_fast(n)
            fast_span.set_attribute("n", n)
            fast_span.set_attribute("nth_fibonacci", ans)
    return HttpResponse(f'F({n}) is: ({ans})')
