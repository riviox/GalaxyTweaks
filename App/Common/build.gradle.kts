plugins {
    kotlin("multiplatform")
    id("org.jetbrains.compose")
}

kotlin {
    jvm()

    sourceSets {
        commonMain {
            dependencies {
                implementation(compose.material3)
                implementation(compose.materialIconsExtended)
                implementation("dev.chrisbanes.material3:material3-window-size-class-multiplatform:0.3.1")
            }
        }
    }
}