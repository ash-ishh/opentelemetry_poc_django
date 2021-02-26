import os
from opentelemetry import trace
from opentelemetry.exporter.jaeger import JaegerSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.instrumentation.django import DjangoInstrumentor


def post_fork(server, worker):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opentelemetry_poc_django.settings")
    server.log.info("Worker spawned (pid: %s)", worker.pid)
    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer_provider().add_span_processor(
        BatchExportSpanProcessor(JaegerSpanExporter(
            service_name='fibonacci',
            insecure=True,
            transport_format="protobuf"
        ))
    )
    DjangoInstrumentor().instrument()
