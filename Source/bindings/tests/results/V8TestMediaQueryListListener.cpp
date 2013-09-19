/*
    This file is part of the Blink open source project.
    This file has been auto-generated by CodeGeneratorV8.pm. DO NOT MODIFY!

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Library General Public
    License as published by the Free Software Foundation; either
    version 2 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Library General Public License for more details.

    You should have received a copy of the GNU Library General Public License
    along with this library; see the file COPYING.LIB.  If not, write to
    the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
    Boston, MA 02111-1307, USA.
*/

#include "config.h"
#include "V8TestMediaQueryListListener.h"

#include "RuntimeEnabledFeatures.h"
#include "bindings/v8/ExceptionMessages.h"
#include "bindings/v8/ExceptionState.h"
#include "bindings/v8/ScriptController.h"
#include "bindings/v8/V8Binding.h"
#include "bindings/v8/V8DOMConfiguration.h"
#include "bindings/v8/V8DOMWrapper.h"
#include "core/css/MediaQueryListListener.h"
#include "core/dom/ContextFeatures.h"
#include "core/dom/Document.h"
#include "core/platform/chromium/TraceEvent.h"
#include "wtf/UnusedParam.h"

namespace WebCore {

static void initializeScriptWrappableForInterface(TestMediaQueryListListener* object)
{
    if (ScriptWrappable::wrapperCanBeStoredInObject(object))
        ScriptWrappable::setTypeInfoInObject(object, &V8TestMediaQueryListListener::info);
    else
        ASSERT_NOT_REACHED();
}

} // namespace WebCore

// In ScriptWrappable::init, the use of a local function declaration has an issue on Windows:
// the local declaration does not pick up the surrounding namespace. Therefore, we provide this function
// in the global namespace.
// (More info on the MSVC bug here: http://connect.microsoft.com/VisualStudio/feedback/details/664619/the-namespace-of-local-function-declarations-in-c)
void webCoreInitializeScriptWrappableForInterface(WebCore::TestMediaQueryListListener* object)
{
    WebCore::initializeScriptWrappableForInterface(object);
}

namespace WebCore {
WrapperTypeInfo V8TestMediaQueryListListener::info = { V8TestMediaQueryListListener::GetTemplate, V8TestMediaQueryListListener::derefObject, 0, 0, 0, V8TestMediaQueryListListener::installPerContextPrototypeProperties, 0, WrapperTypeObjectPrototype };

namespace TestMediaQueryListListenerV8Internal {

template <typename T> void V8_USE(T) { }

static void methodMethod(const v8::FunctionCallbackInfo<v8::Value>& args)
{
    if (UNLIKELY(args.Length() < 1)) {
        throwTypeError(ExceptionMessages::failedToExecute("method", "TestMediaQueryListListener", ExceptionMessages::notEnoughArguments(1, args.Length())), args.GetIsolate());
        return;
    }
    TestMediaQueryListListener* imp = V8TestMediaQueryListListener::toNative(args.Holder());
    V8TRYCATCH_VOID(RefPtr<MediaQueryListListener>, listener, MediaQueryListListener::create(ScriptValue(args[0], args.GetIsolate())));
    imp->method(listener);

    return;
}

static void methodMethodCallback(const v8::FunctionCallbackInfo<v8::Value>& args)
{
    TRACE_EVENT_SET_SAMPLING_STATE("Blink", "DOMMethod");
    TestMediaQueryListListenerV8Internal::methodMethod(args);
    TRACE_EVENT_SET_SAMPLING_STATE("V8", "Execution");
}

} // namespace TestMediaQueryListListenerV8Internal

static const V8DOMConfiguration::MethodConfiguration V8TestMediaQueryListListenerMethods[] = {
    {"method", TestMediaQueryListListenerV8Internal::methodMethodCallback, 0, 1},
};

static v8::Handle<v8::FunctionTemplate> ConfigureV8TestMediaQueryListListenerTemplate(v8::Handle<v8::FunctionTemplate> desc, v8::Isolate* isolate, WrapperWorldType currentWorldType)
{
    desc->ReadOnlyPrototype();

    v8::Local<v8::Signature> defaultSignature;
    defaultSignature = V8DOMConfiguration::installDOMClassTemplate(desc, "TestMediaQueryListListener", v8::Local<v8::FunctionTemplate>(), V8TestMediaQueryListListener::internalFieldCount,
        0, 0,
        V8TestMediaQueryListListenerMethods, WTF_ARRAY_LENGTH(V8TestMediaQueryListListenerMethods), isolate, currentWorldType);
    UNUSED_PARAM(defaultSignature);
    v8::Local<v8::ObjectTemplate> instance = desc->InstanceTemplate();
    v8::Local<v8::ObjectTemplate> proto = desc->PrototypeTemplate();
    UNUSED_PARAM(instance);
    UNUSED_PARAM(proto);

    // Custom toString template
    desc->Set(v8::String::NewSymbol("toString"), V8PerIsolateData::current()->toStringTemplate());
    return desc;
}

v8::Handle<v8::FunctionTemplate> V8TestMediaQueryListListener::GetTemplate(v8::Isolate* isolate, WrapperWorldType currentWorldType)
{
    V8PerIsolateData* data = V8PerIsolateData::from(isolate);
    V8PerIsolateData::TemplateMap::iterator result = data->templateMap(currentWorldType).find(&info);
    if (result != data->templateMap(currentWorldType).end())
        return result->value.newLocal(isolate);

    TRACE_EVENT_SCOPED_SAMPLING_STATE("Blink", "BuildDOMTemplate");
    v8::HandleScope handleScope(isolate);
    v8::Handle<v8::FunctionTemplate> templ =
        ConfigureV8TestMediaQueryListListenerTemplate(data->rawTemplate(&info, currentWorldType), isolate, currentWorldType);
    data->templateMap(currentWorldType).add(&info, UnsafePersistent<v8::FunctionTemplate>(isolate, templ));
    return handleScope.Close(templ);
}

bool V8TestMediaQueryListListener::HasInstance(v8::Handle<v8::Value> value, v8::Isolate* isolate, WrapperWorldType currentWorldType)
{
    return V8PerIsolateData::from(isolate)->hasInstance(&info, value, currentWorldType);
}

bool V8TestMediaQueryListListener::HasInstanceInAnyWorld(v8::Handle<v8::Value> value, v8::Isolate* isolate)
{
    return V8PerIsolateData::from(isolate)->hasInstance(&info, value, MainWorld)
        || V8PerIsolateData::from(isolate)->hasInstance(&info, value, IsolatedWorld)
        || V8PerIsolateData::from(isolate)->hasInstance(&info, value, WorkerWorld);
}

v8::Handle<v8::Object> V8TestMediaQueryListListener::createWrapper(PassRefPtr<TestMediaQueryListListener> impl, v8::Handle<v8::Object> creationContext, v8::Isolate* isolate)
{
    ASSERT(impl.get());
    ASSERT(!DOMDataStore::containsWrapper<V8TestMediaQueryListListener>(impl.get(), isolate));
    if (ScriptWrappable::wrapperCanBeStoredInObject(impl.get())) {
        const WrapperTypeInfo* actualInfo = ScriptWrappable::getTypeInfoFromObject(impl.get());
        // Might be a XXXConstructor::info instead of an XXX::info. These will both have
        // the same object de-ref functions, though, so use that as the basis of the check.
        RELEASE_ASSERT_WITH_SECURITY_IMPLICATION(actualInfo->derefObjectFunction == info.derefObjectFunction);
    }

    v8::Handle<v8::Object> wrapper = V8DOMWrapper::createWrapper(creationContext, &info, toInternalPointer(impl.get()), isolate);
    if (UNLIKELY(wrapper.IsEmpty()))
        return wrapper;

    installPerContextProperties(wrapper, impl.get(), isolate);
    V8DOMWrapper::associateObjectWithWrapper<V8TestMediaQueryListListener>(impl, &info, wrapper, isolate, WrapperConfiguration::Independent);
    return wrapper;
}

void V8TestMediaQueryListListener::derefObject(void* object)
{
    fromInternalPointer(object)->deref();
}

} // namespace WebCore
