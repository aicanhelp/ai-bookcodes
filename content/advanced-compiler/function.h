//
// Created by modongsong on 22-7-27.
//

#pragma once

#define FIRST_OPTON
#ifdef FIRST_OPTON
#define MULTIPLIER (3.0)
#else
#define MULTIPLIER (2.0)
#endif

float add_and_multiply(float x,float y);
