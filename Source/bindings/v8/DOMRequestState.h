/*
 * Copyright (C) 2012 Google Inc. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1.  Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 * 2.  Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY APPLE AND ITS CONTRIBUTORS "AS IS" AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL APPLE OR ITS CONTRIBUTORS BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 * THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef DOMRequestState_h
#define DOMRequestState_h

#include "bindings/v8/DOMWrapperWorld.h"
#include "bindings/v8/V8Binding.h"
#include "core/dom/ScriptExecutionContext.h"
#include "v8.h"
#include "wtf/RefPtr.h"

namespace WebCore {

class DOMRequestState {
public:
    explicit DOMRequestState(ScriptExecutionContext* scriptExecutionContext)
        : m_scriptExecutionContext(scriptExecutionContext)
        , m_world(DOMWrapperWorld::current())
        , m_isolate(toIsolate(scriptExecutionContext))
    {
    }

    void clear()
    {
        m_scriptExecutionContext = 0;
        m_world.clear();
    }

    class Scope {
    public:
        explicit Scope(DOMRequestState& state)
            : m_handleScope(state.isolate())
            , m_contextScope(state.context())
        {
        }
    private:
        v8::HandleScope m_handleScope;
        v8::Context::Scope m_contextScope;
    };

    v8::Local<v8::Context> context()
    {
        return toV8Context(m_scriptExecutionContext, m_world.get());
    }

    v8::Isolate* isolate() const
    {
        return m_isolate;
    }

private:
    ScriptExecutionContext* m_scriptExecutionContext;
    RefPtr<DOMWrapperWorld> m_world;
    v8::Isolate* m_isolate;
};

}
#endif
