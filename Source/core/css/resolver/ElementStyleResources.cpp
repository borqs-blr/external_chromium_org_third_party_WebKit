/*
 * Copyright (C) 1999 Lars Knoll (knoll@kde.org)
 * Copyright (C) 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011 Apple Inc. All rights reserved.
 * Copyright (C) 2013 Google Inc. All rights reserved.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public License
 * along with this library; see the file COPYING.LIB.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
 * Boston, MA 02110-1301, USA.
 *
 */

#include "config.h"
#include "core/css/resolver/ElementStyleResources.h"

#include "core/platform/graphics/filters/FilterOperation.h"

namespace WebCore {

ElementStyleResources::ElementStyleResources()
    : m_hasPendingShaders(false)
    , m_deviceScaleFactor(1)
{
}

void ElementStyleResources::addPendingImageProperty(const CSSPropertyID& property, CSSValue* value)
{
    m_pendingImageProperties.set(property, value);
}

void ElementStyleResources::addPendingSVGDocument(FilterOperation* filterOperation, CSSSVGDocumentValue* cssSVGDocumentValue)
{
    m_pendingSVGDocuments.set(filterOperation, cssSVGDocumentValue);
}

void ElementStyleResources::clear()
{
    m_pendingImageProperties.clear();
    m_pendingSVGDocuments.clear();
    m_hasPendingShaders = false;
    m_deviceScaleFactor = 1;
}

}